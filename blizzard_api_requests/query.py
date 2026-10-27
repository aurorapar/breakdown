from abc import ABC, abstractmethod

import requests

import constants
import log
from oauth import obtain_oauth_token
import sensitive
import settings

user_settings = settings.Settings()

logger = log.get_logger()

REQUEST_DOMAIN = f"https://{getattr(user_settings, constants.REGION)}.api.blizzard.com/data/wow/"
REQUEST_NAMESPACE = f"{{0}}-{getattr(user_settings, constants.GAME_VERSION)}{constants.DEFAULT_REGION}"
REQUEST_HEADER = {
    "Battlenet-Namespace": REQUEST_NAMESPACE,
    constants.AUTHORIZATION: "Bearer {0}".format(sensitive.secrets[constants.TOKEN])
}


class Query(ABC):

    REQUIRED_ATTRIBUTES = [constants.ENDPOINT, constants.NAMESPACE]

    def __init__(self, endpoint, namespace):
        self.endpoint = endpoint
        self.namespace = namespace

    def __setattr__(self, k, v):
        if v is None and k in Query.REQUIRED_ATTRIBUTES:
            raise ValueError(f"Required attribute {k} not initialized")
        object.__setattr__(self, k, v)

    def __getattribute__(self, k):
        v = super().__getattribute__(k)
        logger.info(f"Query attribute {k} set to {v}")
        if v is None and k in Query.REQUIRED_ATTRIBUTES:
            raise ValueError(f"Required attribute {k} not initialized")

        match k:

            case constants.ENDPOINT:
                if v not in constants.VALID_ENDPOINTS.values():
                    raise ValueError(f"{k} not a valid endpoint")
                return v

            case _:
                return v

    def perform_request(self, **kwargs):
        obtain_oauth_token()
        params = kwargs

        domain = REQUEST_DOMAIN + self.endpoint + "namespace=" + REQUEST_NAMESPACE.format(self.namespace)

        headers = REQUEST_HEADER.copy()
        headers[constants.AUTHORIZATION].format(sensitive.secrets[constants.TOKEN])
        headers["Battlenet-Namespace"].format(self.namespace)

        results = []
        data = self.__do_query(domain, headers, params)
        results += data['results']

        page_count = int(data['pageCount'])
        if page_count != 1:
            for x in range(2, page_count):
                params['pageCount'] = x
                new_data = self.__do_query(domain, headers, params)
                results += new_data['results']

                if x == 10 and int(new_data['pageResults']) > int(new_data['maxPageSize']):
                    raise RuntimeWarning("Maximum page size exceeded in response")

        return results

    def __do_query(self, domain, headers, params):
        response = requests.get(domain, headers=headers, params=params)
        if response.status_code != requests.codes.ok:
            raise RuntimeError(f"Query failed: {response.status_code} {response.reason}\n\t{response.url}")

        logger.info(response.request.url)
        logger.info(response.request.body)
        logger.info(response.request.headers)

        data = response.json()
        return data
    
    @abstractmethod
    def execute(self):
        pass
