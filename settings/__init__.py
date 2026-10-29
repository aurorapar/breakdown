import json
import os

import constants

DEFAULT = {
            constants.LANGUAGE: None,
            constants.REGION: None,
            constants.GAME_VERSION: None,
            constants.GUI_GEOMETRY: "640x480",

            constants.BACKGROUND_COLOR: "#303030",
            constants.TEXT_COLOR: "#FFFFFF",
            constants.WINDOW_SIZE: "300x200",
            constants.WINDOW_X: "300",
            constants.WINDOW_Y: "300",

        }

class Settings:

    def __init__(self):

        self.saveable = DEFAULT

        self.__load_settings()

    def __load_settings(self):
        self.__initialize_settings()

        with open(constants.SETTINGS_CACHE, 'r') as f:
            loaded_settings = json.load(f)

        for k,v in self.saveable.items():
            if k not in loaded_settings:
                loaded_settings[k] = v

        self.saveable = loaded_settings

    def __save_settings(self):
        with open(constants.SETTINGS_CACHE, 'w') as f:
            json.dump(self.saveable, f)


    def __initialize_settings(self):
        if not os.path.exists(constants.SETTINGS_CACHE):
            self.__save_settings()


    def __getattr__(self, name):
        if name in object.__getattribute__(self, "saveable"):
            return  object.__getattribute__(self, "saveable")[name]
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if not hasattr(self, "saveable"):
            object.__setattr__(self, "saveable", DEFAULT)
            return
        if name in self.saveable:
            saveable = self.saveable
            saveable[name] = value
            object.__setattr__(self, "saveable", saveable)
        else:
            object.__setattr__(self, name, value)
        self.__save_settings()