import json
import time

import gui
from blizzard_api_requests import QueryDeCrafts, QueryAuction
import constants
import log
from wowhead_requests import QueryItemWowhead

logger = log.get_logger()

def workflow():
    main_window = gui.root
    main_window.mainloop()
    exit()

    disenchantable_items = get_disenchantable_items()    

    wowhead_items = get_wowhead_data(disenchantable_items)

    craftable_items = filter_crafted_items(wowhead_items)
    del wowhead_items
    del disenchantable_items

    auction_data = get_auction_data()

    exit()


def get_disenchantable_items():
    deable_items = []
    disenchantable_items_query = QueryDeCrafts()
    for quality in constants.QUALITIES:
        for subclass in constants.ITEM_SUBCLASSES:
            deable_items += disenchantable_items_query.execute(quality, subclass)
            break
        break
    #with open(constants.DISENCHANTABLE_CRAFT_ITEM_CACHE, "w") as f:
    #    json.dump(deable_items, f)

    #with open(constants.DISENCHANTABLE_CRAFT_ITEM_CACHE, "r") as f:
    #    deable_items = json.load(f)

    return deable_items

def get_wowhead_data(item_data):
    q = QueryItemWowhead()

    with open(constants.WOWHEAD_ITEM_CACHE, "r") as f:
        cache = json.load(f)

    wowhead_items = []
    for index, item_data in enumerate(item_data):
        item_id = item_data[constants.DATA][constants.ID]
        if item_id in cache.keys():
            continue

        time.sleep(.1)  # be nice on their api
        sleep_time = 10
        failed_runs = 0
        run = True

        while run:

            try:
                r = q.execute(item_id)

                if constants.ERROR in r[constants.WOWHEAD]:
                    logger.error(r[constants.WOWHEAD][constants.ERROR])
                    logger.error(
                        f"{item_id} - {item_data[constants.DATA][constants.NAME]}")
                else:
                    cache[item_id] = r[constants.WOWHEAD][constants.ITEM]

                    with open(constants.WOWHEAD_ITEM_CACHE, "w") as f:
                        json.dump(cache, f)

                failed_runs = 0
                break

            except RuntimeError as e:
                if "forbidden" in str(e).lower():
                    failed_runs += 1
                    time_to_sleep = sleep_time * failed_runs
                    print(f"Wowhead denied request, sleeping {time_to_sleep}s")
                    time.sleep(sleep_time * failed_runs)
                else:
                    raise e

    return cache


def filter_crafted_items(item_data):
    craftables = [x for x in item_data if 'createdBy' in item_data[constants.WOWHEAD][constants.ITEM]]
    with open(constants.CRAFTABLE_ITEM_CACHE, "w") as f:
        json.dump(craftables, f)
    return craftables


def get_auction_data():
    q = QueryAuction()
    auctions = q.execute()


def get_realm_id():
    q = QueryRealms()
    realms = q.execute()