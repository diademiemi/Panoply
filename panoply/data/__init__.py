from data.sources import command, homeassistant
import config

import threading

allData = {}

def start():
    web_data()
    local_data()
    
def web_data():
    if config.HOME_ASSISTANT_STATE_PLACEHOLDERS:
        for key, value in config.HOME_ASSISTANT_STATE_PLACEHOLDERS.items():
            allData[key] = homeassistant.getState(value)
    threading.Timer(config.WEB_REFRESH_INTERVAL, web_data).start()

def local_data():
    if config.COMMAND_PLACEHOLDERS:
        for key, value in config.COMMAND_PLACEHOLDERS.items():
            print(key)
            print(value)
            print(command.getOutput(value))
            allData[key] = command.getOutput(value)
    threading.Timer(config.LOCAL_REFRESH_INTERVAL, local_data).start()

def getData():
    return allData
