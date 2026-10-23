import json

import constants


with open(constants.__SECRETS_FILE, 'r') as f:
    secrets = json.load(f)

CLIENT_ID = secrets[constants.CLIENT_ID]
CLIENT_SECRET = secrets[constants.CLIENT_SECRET]
TOKEN = None
TOKEN_DURATION = None


def save_secrets():
    with open(constants.__SECRETS_FILE, 'w') as f:
        json.dump(secrets, f)


def set_token(token, duration):
    global TOKEN, TOKEN_DURATION
    TOKEN, TOKEN_DURATION = token, duration

    secrets[constants.TOKEN] = TOKEN
    secrets[constants.TOKEN_DURATION] = TOKEN_DURATION

    with open(constants.__SECRETS_FILE, 'w') as f:
        json.dump(secrets, f)
