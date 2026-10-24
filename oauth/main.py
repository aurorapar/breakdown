from log import get_logger

import requests

import constants
import sensitive



def obtain_oauth_token():
    log = get_logger()
    log.info("Starting OAuth")

    data = {
        'grant_type': 'client_credentials',
    }
    secrets = (sensitive.CLIENT_ID, sensitive.CLIENT_SECRET)

    response = requests.post('https://oauth.battle.net/token', data=data, auth=secrets)
    if response.status_code not in [200]:
        e = f"Response code {response.status_code} not in accepted values.\n{response.ok}\n{response.reason}"
        raise RuntimeError(e)

    data = response.json()
    log.info(data)

    if int(sensitive.secrets[constants.TOKEN_DURATION]) != int(data['expires_in']) or data['access_token'] != sensitive.secrets[constants.TOKEN]:
        log.info("OAuth token updated")
        sensitive.set_token(data['access_token'], int(data['expires_in']))

