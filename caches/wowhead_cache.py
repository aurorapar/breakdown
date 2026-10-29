import json
import os
import time
import traceback

import constants
import log
from caches import BlizzardItemCache
from wowhead_requests import QueryItemWowhead
from caches.cache import Cache

logger = log.get_logger()


class WowheadCache(Cache):

    def __init__(self):
        super().__init__(constants.WOWHEAD_DATA, constants.WOWHEAD_ITEM_CACHE)


    def load(self):
        if not os.path.exists(self.file_location):
            self.data = {
                constants.DATA: {}  # dict instead of list
            }
            self.save()
        with open(self.file_location, 'r') as f:
            return json.load(f)

    def populate(self, callback=None, root=None):
        blizzard_cache = BlizzardItemCache()
        item_count = len(blizzard_cache.data[constants.DATA])
        for i, item_data in enumerate(blizzard_cache.data[constants.DATA]):
            item_id = item_data[constants.ID]
            if item_id in self.data[constants.DATA]:
                if int(time.time()) - item_id[constants.LAST_UPDATED] < 86400: #  no need to update more than a day
                    continue

            sleep_time = 5 / 2
            while True:
                try:
                    self.perform_query(item_id)
                    if callback:
                        callback(f"Progress: {i/item_count * 100:.0f}% of ")
                    sleep_time = max(5/2, sleep_time/2)
                    break
                except Exception as e:
                    traceback.print_exc()
                    sleep_time *= 2
                    logger.info(f"Delaying query for {int(sleep_time)}s")
                    root.after(int(sleep_time) * 1000)

    def perform_query(self, item_id):
        q = QueryItemWowhead()
        try:
            r = q.execute(item_id)
            if not r:
                return
            if constants.ERROR in r[constants.WOWHEAD]:
                logger.error(f"{item_id}" + r[constants.WOWHEAD][constants.ERROR])
            else:
                self.add_item({item_id: r[constants.WOWHEAD][constants.ITEM]})
                self.count = len(self.data[constants.DATA].keys())

        except RuntimeError as e:
            if "forbidden" in str(e).lower():
                logger.error(f"Wowhead denied request. Increase time between requests")
            raise e
