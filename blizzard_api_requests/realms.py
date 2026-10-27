
import constants
from blizzard_api_requests.query import Query

class QueryRealms(Query):

    def __init__(self):
        self.endpoint = constants.VALID_ENDPOINTS
        super().__init__(endpoint=constants.VALID_ENDPOINTS[constants.REALMS], namespace=constants.Namespace.STATIC)
    