import tkinter as tk
from tkinter import ttk, StringVar

import constants
import log
import settings

logger = log.get_logger()

class DropDown:

    def __init__(self, master, setting_name, setting_enum, setting_labels=None, *args, **kwargs):
        self.master = master
        super().__init__()
        user_settings = settings.Settings()
        self.setting_name = setting_name
        self.setting_labels = setting_labels
        self.setting_enum = setting_enum

        label = tk.Label(master, text=self.setting_name)
        label.configure(bg=getattr(user_settings, constants.BACKGROUND_COLOR), fg=getattr(user_settings, constants.TEXT_COLOR))


        setting_options = list(self.setting_labels.values()) if self.setting_labels else [x.value for x in setting_enum]
        current_selection = getattr(user_settings, self.setting_name)
        default_selection = StringVar(master)
        if current_selection is not None:
            if self.setting_labels:
                default_selection.set([v for k,v in self.setting_labels.items() if k.value == current_selection][0])
            else:
                current_selection = [e.value for e in self.setting_enum if e.value == current_selection][0]
                default_selection.set(current_selection or setting_options[0])
        else:
            current_selection = setting_options[0]
            default_selection.set(setting_options[0])

        setting_dropdown = tk.OptionMenu(master, default_selection, *setting_options, command=self.dropdown_callback)
        setting_dropdown.configure(bg=getattr(user_settings, constants.BACKGROUND_COLOR), fg=getattr(user_settings, constants.TEXT_COLOR))

        master.add_column_item(label)
        master.add_column_item(setting_dropdown)

    def dropdown_callback(self, selection):
        if self.setting_labels:
            new_setting = [k.value for k, v in self.setting_labels.items() if v == selection][0]
        else:
            new_setting = selection

        user_settings = settings.Settings()
        setattr(user_settings, self.setting_name, new_setting)
