from logging import getLogger

import requests

import constants
import sensitive



def obtain_oauth_token():
    log = getLogger(__name__)
    log.info("Starting OAuth")

    if sensitive.secrets[constants.TOKEN_DURATION] > 0:
        log.info(f"Returning cached token (duration {sensitive.secrets[constants.TOKEN_DURATION]} seconds)")
        return

    data = {
        'grant_type': 'client_credentials',
    }
    secrets = (sensitive.CLIENT_ID, sensitive.CLIENT_SECRET)

    response = requests.post('https://oauth.battle.net/token', data=data, auth=secrets)
    if response.status_code not in [200]:
        e = f"Response code {response.status_code} not in accepted values.\n{response.ok}\n{response.reason}"
        raise RuntimeError(e)

    data = response.json()
    sensitive.set_token(data['access_token'], int(data['expires_in']))
