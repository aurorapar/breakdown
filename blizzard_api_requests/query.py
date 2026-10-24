from abc import ABC

import requests

import constants
import log
import sensitive

logger = log.get_logger()

REQUEST_DOMAIN = f"https://{constants.REGION}.api.blizzard.com/data/wow/"
REQUEST_NAMESPACE = f"static-classic1x-{constants.REGION}"
REQUEST_HEADER = {
    "Battlenet-Namespace": REQUEST_NAMESPACE,
    constants.AUTHORIZATION: "Bearer {0}".format(sensitive.secrets[constants.TOKEN])
}


VALID_ENDPOINTS = {
    constants.ITEM_SEARCH: "search/item?"
}


class Query(ABC):

    REQUIRED_ATTRIBUTES = [constants.ENDPOINT]

    def __init__(self, endpoint):

        self.endpoint = endpoint

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
                if v not in VALID_ENDPOINTS.values():
                    raise ValueError(f"{k} not a valid endpoint")
                return v

            case _:
                return v

    def perform_request(self, **kwargs):
        params = kwargs

        domain = REQUEST_DOMAIN + self.endpoint + "namespace=" + REQUEST_NAMESPACE

        headers = REQUEST_HEADER.copy()
        headers[constants.AUTHORIZATION].format(sensitive.secrets[constants.TOKEN])

        response = requests.get(domain, headers=headers, params=params)
        if response.status_code != requests.codes.ok:
            raise RuntimeError(f"Query failed: {response.status_code} {response.reason}\n\t{response.url}")

        logger.info(response.request.url)
        logger.info(response.request.body)
        logger.info(response.request.headers)
        logger.info(response.json())
        return response.json()
