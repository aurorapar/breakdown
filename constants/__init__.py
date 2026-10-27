import enum

PROJECT_NAME = "BREAKDOWN"

NAME = "name"
DATA = "data"
ID = "id"
ITEM = "item"
ERROR = "error"
QUANTITY = "quantity"
COUNT = "count"
SPELL = "spell"
REAGENT = "reagent"
LANGUAGE = "Language"
GUI_GEOMETRY = "geometry"
LAST_UPDATED = "last_updated"

BACKGROUND_COLOR = "background_color"
TEXT_COLOR = "text_color"

__SECRETS_FILE = "secrets.json"
CLIENT_ID = "client_id"
CLIENT_SECRET = "client_secret"
TOKEN = "token"
TOKEN_DURATION = "token_duration"

DEFAULT_REGION = "us"
ENDPOINT = "endpoint"
LANG = "en_US"
NAMESPACE = "namespace"
WOWHEAD = "wowhead"


QUALITY = "quality"
UNCOMMON = "Uncommon"
RARE = "Rare"
EPIC = "Epic"
QUALITIES = [UNCOMMON, RARE, EPIC]

ITEM_CLASS = "item_class"
ITEM_SUBCLASS = "item_subclass"

ARMOR = "Armor"
WEAPON = "Weapon"
AXE = "Axe"
BOW = "Bow"
MACE = "Mace"
POLEARM = "Polearm"
SWORD = "Sword"
STAFF = "Staff"
EXOTIC = "Exotic"
FIST_WEAPON = "Fist Weapon"
DAGGER = "Dagger"
THROWN = "Thrown"
SPEAR = "Spear"
CROSSBOW = "Crossbow"
WAND = "Wand"
FISHING_POLE = "Fishing Pole"
CLOTH = "Cloth"
LEATHER = "Leather"
MAIL = "Mail"
PLATE = "Plate"
ITEM_SUBCLASSES = [AXE, BOW, MACE, POLEARM, SWORD, STAFF, EXOTIC, FIST_WEAPON, DAGGER, THROWN, SPEAR, CROSSBOW, WAND,
                   FISHING_POLE, CLOTH, LEATHER, MAIL, PLATE]

ITEM_SEARCH = "item_search"
AUCTIONS = "auctions"
REALMS = "realms"

AUTHORIZATION = "Authorization"

DISENCHANTABLE_CRAFT_ITEM_CACHE = "disenchantable_crafts.json"
WOWHEAD_ITEM_CACHE = "wowhead.json"
CRAFTABLE_ITEM_CACHE = "craftables.json"
SETTINGS_CACHE = "settings.json"

VALID_ENDPOINTS = {
    ITEM_SEARCH: "search/item?",
    AUCTIONS: "{0}/auctions",
    REALMS: "search/connected-realm",
}

class Namespace(enum.Enum):
    STATIC = "static"
    DYNAMIC = "dynamic"
    PROFILE = "profile"

class Region(enum.Enum):
    US = "us"
    EU = "eu"
    KR = "kr"
    TW = "tw"
    CN = "cn"

REGION = "Region"
REGION_LABELS = {
    Region.US: "United States",
    Region.EU: "Europe",
    Region.KR: "Korea",
    Region.TW: "Taiwan",
    Region.CN: "China",
}

class GameVersion(enum.Enum):
    CLASSIC_ERA = "classic1x-"
    CLASSIC_PROGRESSION = "classic-"
    BURNING_CRUSADE = "classicann-"
    RETAIL = ""

GAME_VERSION = "Game Version"
GAME_VERSION_LABELS = {
    GameVersion.CLASSIC_ERA: "Classic",
    GameVersion.BURNING_CRUSADE: "Burning Crusade",
    GameVersion.CLASSIC_PROGRESSION: "Classic Progression",
    GameVersion.RETAIL: "Retail",
}

class LanguageLabel(enum.Enum):
    en_US = "English (United States)"
    en_GB = "English (Great Britain)"
    it_IT = "Italiano"
    ru_RU = "Русский"
    zh_TW = "臺灣話"
    ko_KR = "한국어"
    es_MX = "Español (Mexico)"
    pt_BR = "Portuguesa (Brasil)"
    de_DE = "Deutsch"
    es_ES = "Español (España)"
    fr_FR = "Français"
    zh_CN = "普通话"
