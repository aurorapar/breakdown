import constants
import settings



def handle_game_version_selection(selection):
    new_setting = [k.value for k,v in constants.GAME_VERSION_LABELS.items() if v == selection][0]

    user_settings = settings.Settings()
    setattr(user_settings, constants.GAME_VERSION, new_setting)

def handle_region_selection(selection):
    new_setting = [k.value for k, v in constants.REGION_LABELS.items() if v == selection][0]

    user_settings = settings.Settings()
    setattr(user_settings, constants.REGION, new_setting)

def handle_language_selection(selection):
    new_setting = [l.value for l in constants.LanguageLabel if l.value == selection][0]

    user_settings = settings.Settings()
    setattr(user_settings, constants.LANGUAGE, new_setting)