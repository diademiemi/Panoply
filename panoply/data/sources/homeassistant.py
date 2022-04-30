import config

import json
from requests import get

def getState(entity):
    headers = {
        "Authorization": "Bearer {key}".format(key = config.HOME_ASSISTANT_KEY),
        "content-type": "application/json",
    }

    endpoint = "{url}/api/states/{entity}".format(url = config.HOME_ASSISTANT_URL, entity = entity)
    
    try:
        response = get(endpoint, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data["state"]
        else:
            return "ERROR"
    except:
        return "ERROR"
        
def getColor(entity):
    headers = {
        "Authorization": "Bearer {key}".format(key = config.HOME_ASSISTANT_KEY),
        "content-type": "application/json",
    }

    endpoint = "{url}/api/states/{entity}".format(url = config.HOME_ASSISTANT_URL, entity = entity)
    
    try:
        response = get(endpoint, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            if "rgb_color" in data["attributes"]:
                return data["attributes"]["rgb_color"]
            else:
                return (0, 0, 0)
        else:
            return (0, 0, 0)
    except:
        return (0, 0, 0)