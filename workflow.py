import json

from blizzard_api_requests import QueryDeCrafts
import constants

def workflow():
    q = QueryDeCrafts()
    disenchantable_items = q.perform_request()

    with open(constants.DISENCHANTABLE_CRAFT_ITEM_CACHE, "w") as f:
        json.dump(disenchantable_items, f)

