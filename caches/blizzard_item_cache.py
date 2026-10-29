import constants
from blizzard_api_requests import QueryDeCrafts
from caches.cache import Cache
import log

logger = log.get_logger()


class BlizzardItemCache(Cache):

    def __init__(self):
        super().__init__(constants.BLIZZARD_ITEM_DATA, constants.DISENCHANTABLE_CRAFT_ITEM_CACHE)

    def populate(self, callback=None, root=None):
        logger.info("Populated called")
        self.data[constants.DATA] = []
        self.count = 0
        callback(self.count)
        disenchantable_items_query = QueryDeCrafts()

        for quality in constants.QUALITIES:
            for subclass in constants.ITEM_SUBCLASSES:
                results = disenchantable_items_query.execute(quality, subclass)
                for result in results:
                    self.add(result[constants.DATA])
                    self.count += len(result[constants.DATA])
                    if callback:
                        callback(self.count)
