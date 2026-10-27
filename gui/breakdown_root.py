import tkinter as tk

import constants
from gui import breakdown_dropdowns, breakdown_frame, dropdown_container
import settings

user_settings = settings.Settings()


class BdRoot(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title(constants.PROJECT_NAME)
        self.geometry(user_settings.geometry)
        self.minsize(320, 240)

        self.configure(background = getattr(user_settings, constants.BACKGROUND_COLOR))

        settings_dropdown_frame = dropdown_container.DropdownContainer(self, height=20, width=300)
        language_dropdown = breakdown_dropdowns.DropDown(settings_dropdown_frame, constants.LANGUAGE,
                                                             constants.LanguageLabel)

        game_version_dropdown = breakdown_dropdowns.DropDown(settings_dropdown_frame, constants.GAME_VERSION,
                                                             constants.GameVersion, constants.GAME_VERSION_LABELS)

        region_dropdown = breakdown_dropdowns.DropDown(settings_dropdown_frame, constants.REGION,
                                                             constants.Region, constants.REGION_LABELS)

        settings_dropdown_frame.pack(anchor="nw")
        
        breakdown_mainframe = breakdown_frame.BreakdownFrame(self)
        breakdown_mainframe.configure(background = "#303030")
        breakdown_mainframe.pack()
        