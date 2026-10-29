import time

import constants
from blizzard_api_requests import Query
import log

logger = log.get_logger()


class QueryDeCrafts(Query):

    def __init__(self):
        logger.info(f"Endpoint: {constants.VALID_ENDPOINTS[constants.ITEM_SEARCH]}")
        super().__init__(endpoint=constants.VALID_ENDPOINTS[constants.ITEM_SEARCH], namespace=constants.Namespace.STATIC.value)

    def execute(self, quality, subclass):
        req = super().perform_request
        params = {
            f"{constants.QUALITY}.{constants.NAME}.{constants.LANG}": quality,
            f"{constants.ITEM_SUBCLASS}.{constants.NAME}.{constants.LANG}": subclass
        }

        response = req(**params)

        return response