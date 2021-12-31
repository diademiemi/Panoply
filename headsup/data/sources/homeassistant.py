import config

import json
from requests import get

def getTemp():
    headers = {
        "Authorization": "Bearer {key}".format(key = config.HOME_ASSISTANT_KEY),
        "content-type": "application/json",
    }

    endpoint = "{url}/api/states/{entity}".format(url = config.HOME_ASSISTANT_URL, entity = config.HOME_ASSISTANT_TEMP_SENSOR)

    response = get(endpoint, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data["state"]