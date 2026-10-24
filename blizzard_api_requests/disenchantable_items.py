import log

import constants
from blizzard_api_requests import Query
from blizzard_api_requests.query import VALID_ENDPOINTS

logger = log.get_logger()


class QueryDeCrafts(Query):

    def __init__(self):
        logger.info(f"Endpoint: {VALID_ENDPOINTS[constants.ITEM_SEARCH]}")
        super().__init__(endpoint=VALID_ENDPOINTS[constants.ITEM_SEARCH])

    def perform_request(self):
        req = super().perform_request
        params = {
            "quality": ["UNCOMMON", "RARE", "EPIC"],
            "item_subclass.name.en_US": ["TAILORING", "BLACKSMITHING", "LEATHERWORKING", "ENCHANTING"]
        }

        data = []

        for q in params["quality"]:
            for p in params["item_subclass.name.en_US"]:
                req_params = {
                    # "quality": q,
                    # "item_subclass.name.en_US": p,
                    "item_class.name.en_US": 'CLOTH'
                }
                resp = req(**req_params)
                data.append(resp)
                break
            break
        return data