from abc import ABC

import requests
import xmltodict

import constants
import log

logger = log.get_logger()

DOMAIN = "https://wowhead.com/forever/"

VALID_ENDPOINTS = {
    "item": "item={0}&xml"
}

class QueryWowhead(ABC):

    REQUIRED_ATTRIBUTES = [constants.ENDPOINT]

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def __setattr__(self, k, v):
        if v is None and k in QueryWowhead.REQUIRED_ATTRIBUTES:
            raise ValueError(f"Required attribute {k} not initialized")
        object.__setattr__(self, k, v)

    def __getattribute__(self, k):
        v = super().__getattribute__(k)
        if v is None and k in QueryWowhead.REQUIRED_ATTRIBUTES:
            raise ValueError(f"Required attribute {k} not initialized")

        match k:

            case constants.ENDPOINT:
                if v not in VALID_ENDPOINTS.values():
                    raise ValueError(f"{k} not a valid endpoint")
                return v

            case _:
                return v

    def perform_request(self, entity_id):
        domain = DOMAIN
        endpoint = self.endpoint.format(entity_id)
        data = self.__do_query(domain, endpoint)

        return data

    def __do_query(self, domain, endpoint):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:146.0) Gecko/20100101 Firefox/146.0",
            "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, * / *;q = 0.8"
        }
        response = requests.get(domain + endpoint, headers=headers)

        if response.status_code != requests.codes.ok:
            raise RuntimeError(f"Query failed: {response.status_code} {response.reason}\n\t{response.url}")

        logger.info(response.request.url)
        logger.info(response.request.body)
        logger.info(response.request.headers)

        data = response.text.strip()
        data = xmltodict.parse(xml_input=data)
        try:
            _ = data[constants.WOWHEAD][constants.ITEM][constants.CREATED_BY]
            return data
        except KeyError as e:
            return None

