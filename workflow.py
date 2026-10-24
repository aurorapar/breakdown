from blizzard_api_requests import QueryDeCrafts
from oauth import obtain_oauth_token

def workflow():
    obtain_oauth_token()

    q = QueryDeCrafts()
    disenchantable_items = q.perform_request()

