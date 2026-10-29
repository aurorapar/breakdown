import datetime
import json
import os
import time
from abc import abstractmethod, ABC

import constants
import log

logger = log.get_logger()

class Cache(ABC):

    def __init__(self, name, file_location):
        self.name = name
        self.file_location = file_location
        self.data = self.load()
        if not hasattr(self, constants.TIME):
            self.update_time()
        self.count = len(self.data[constants.DATA])

    def save(self):
        self.data[constants.NAME] = self.name
        self.update_time()
        with open(self.file_location, 'w') as f:
            json.dump(self.data, f)

    def load(self):
        if not os.path.exists(self.file_location):
            self.data = {
                constants.DATA: []
            }
            self.save()
        with open(self.file_location, 'r') as f:
            return json.load(f)

    def add(self, item):
        self.data[constants.DATA] += [item]
        self.save()
        self.count = len(self.data[constants.DATA])

    def add_item(self, item):
        print(item)
        for k,v in item.items():
            self.data[constants.DATA][k] = v
        self.save()
        self.count = len(self.data[constants.DATA])

    def update_time(self):
        self.data[constants.LAST_UPDATED] = int(time.time())
        self.time = datetime.datetime.fromtimestamp(self.data[constants.LAST_UPDATED])

    @abstractmethod
    def populate(self, callback=None, root=None):
        logger.info("Base populated called")
