import tkinter as tk

import constants
from blizzard_api_requests import auction
from caches import blizzard_cache, wowhead_cache #, auction_cache
from gui import dropdowns, breakdown_frame, container, cache_info
import settings

def start_gui():
    main_frame = BdRoot(tk.Tk())
    main_frame.configure(bg="#292929")
    main_frame.pack(expand=True, fill="both")
    main_frame.mainloop()

class BdRoot(tk.Frame):

    def __init__(self, master=None):
        user_settings = settings.Settings()
        super().__init__(master)
        self.master.title(constants.PROJECT_NAME)
        self.master.geometry(getattr(user_settings, constants.WINDOW_SIZE))
        self.master.minsize(200, 200)
        self.width = 200

        self.configure(background = getattr(user_settings, constants.BACKGROUND_COLOR))

        self.settings_dropdown_frame = container.Container(self, height=20, width=300)
        language_dropdown = dropdowns.DropDown(self.settings_dropdown_frame, constants.LANGUAGE,
                                               constants.LanguageLabel)

        game_version_dropdown = dropdowns.DropDown(self.settings_dropdown_frame, constants.GAME_VERSION,
                                                   constants.GameVersion, constants.GAME_VERSION_LABELS)

        region_dropdown = dropdowns.DropDown(self.settings_dropdown_frame, constants.REGION,
                                             constants.Region, constants.REGION_LABELS)

        self.settings_dropdown_frame.pack(anchor="nw", pady=(10,0))
        
        self.main_window = breakdown_frame.BreakdownFrame(self)

        # self.cache_frames = []
        # for cache in (blizzard_cache, wowhead_cache):
        #     self.cache_frames.append(cache_info.CacheInfo(self.main_window, cache))
        cache_info.CacheInfo(self.main_window, blizzard_cache).pack(anchor="nw")
        cache_info.CacheInfo(self.main_window, wowhead_cache).pack(anchor="nw")

        self.main_window.pack(expand=True, fill="both", padx=10, pady=10)

        self.bind("<Configure>", self.handle_configure)
        self.bind("<Motion>", self.handle_configure)
        self.bind("<Destroy>", self.handle_configure)

    def handle_configure(self, event=None):
        user_settings = settings.Settings()
        try:
            width = self.settings_dropdown_frame.winfo_width()
            self.master.minsize(width, 200)
        except tk.TclError as e:
            if not 'container' in str(e):
                raise e
        setattr(user_settings, constants.WINDOW_SIZE, self.master.winfo_geometry())

    def all_children(self, window, finList=None, indent=0):
        finList = finList or []
        children = window.winfo_children()
        for item in children:
            finList.append(item)
            self.all_children(item, finList, indent + 1)
        return finList
