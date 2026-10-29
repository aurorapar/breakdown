import threading
import tkinter as tk
import time

import constants
import log
import settings
from gui.container import Container

logger = log.get_logger()

class CacheInfo(Container):

    def __init__(self, master, cache, *args, **kwargs):
        self.master = master
        self.cache = cache
        self.thread = (None,None)
        threading.Thread(target=self.__cleanup, args=(), daemon=True).start()
        super().__init__(self.master,*args, **kwargs)
        user_settings = settings.Settings()

        self.name_label = tk.Label(self, text=cache.name, font=(constants.DEFAULT_FONT,constants.DEFAULT_FONT_SIZE))
        self.name_label.configure(bg=getattr(user_settings, constants.BACKGROUND_COLOR), fg=getattr(user_settings, constants.TEXT_COLOR))

        self.updated_label = tk.Label(self, text=f"{constants.LAST_UPDATED} {cache.time}", font=(constants.DEFAULT_FONT, constants.DEFAULT_FONT_SIZE))
        self.updated_label.configure(bg=getattr(user_settings, constants.BACKGROUND_COLOR),
                             fg=getattr(user_settings, constants.TEXT_COLOR))

        self.count_label = tk.Label(self, text=f"{cache.count} {constants.ITEMS}", font=(constants.DEFAULT_FONT, constants.DEFAULT_FONT_SIZE))
        self.count_label.configure(bg=getattr(user_settings, constants.BACKGROUND_COLOR),
                                fg=getattr(user_settings, constants.TEXT_COLOR))
        self.updating_count = False

        self.update_button = tk.Button(self, text=constants.UPDATE, command=self.update)

        self.add_column_item(self.name_label)
        self.add_column_item(self.updated_label)
        self.add_column_item(self.count_label)
        self.add_column_item(self.update_button)

    def update(self):
        logger.info("Update button clicked")
        self.updated_label.configure(text=constants.UPDATING)
        self.update_button.configure(state=tk.DISABLED)
        self.thread = [threading.Thread(target=self.__update, args=()), True]
        self.thread[0].start()

    def __update(self):
        self.cache.populate(self.__update_count, self.master.master)
        self.updated_label.configure(text=f"{constants.LAST_UPDATED} {self.cache.time}")
        self.update_button.configure(state=tk.NORMAL)
        self.thread[1] = False

    def __update_count(self, new_text):
            self.count_label.configure(text=f"{new_text} {constants.ITEMS}")

    def __cleanup(self):
        if self.thread[0] and not self.thread[1]:
            self.thread[0].join()
            self.thread = (None,None)
