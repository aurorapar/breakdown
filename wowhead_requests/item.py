import wowhead_requests.query as query

class QueryItemWowhead(query.QueryWowhead):

    def __init__(self):
        self.endpoint = query.VALID_ENDPOINTS["item"]
        super().__init__(self.endpoint)

    def execute(self, entity_id):
        return super().perform_request(entity_id)