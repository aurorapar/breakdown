from sensitive import CLIENT_ID, CLIENT_SECRET

import requests

from logging import getLogger


def obtain_oauth_token():
    log = getLogger(__name__)
    log.info("Starting OAuth")



    data = {
        'grant_type': 'client_credentials',
    }
    secrets = (CLIENT_ID, CLIENT_SECRET)

    log.info(f"Using {secrets}")

    raise NotImplementedError("working on things")

    # response = requests.post('https://oauth.battle.net/token', data=data, auth=secrets)