import constants
from blizzard_api_requests import Query

class QueryAuction(Query):
    def __init__(self):
        super().__init__(endpoint=constants.VALID_ENDPOINTS[constants.AUCTIONS], namespace=constants.Namespace.DYNAMIC.value)

    def execute(self, realm_id):
        self.endpoint = self.endpoint.format(realm_id)
        super().perform_request()