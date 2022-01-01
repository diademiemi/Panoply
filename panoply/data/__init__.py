from data.sources import command, homeassistant
import config

import threading

placeholders = {}
colors = {}

def start():
    web_data()
    local_data()
    
def web_data():
    if config.HOME_ASSISTANT_STATE_PLACEHOLDERS:
        for key, value in config.HOME_ASSISTANT_STATE_PLACEHOLDERS.items():
            placeholders[key] = homeassistant.getState(value)
    if config.HOME_ASSISTANT_COLOURS:
        for key, value in config.HOME_ASSISTANT_COLOURS.items():
            colors[key] = homeassistant.getColor(value)
    threading.Timer(config.WEB_REFRESH_INTERVAL, web_data).start()

def local_data():
    if config.COMMAND_PLACEHOLDERS:
        for key, value in config.COMMAND_PLACEHOLDERS.items():
            placeholders[key] = command.getOutput(value)
    threading.Timer(config.LOCAL_REFRESH_INTERVAL, local_data).start()

def getPlaceholders():
    return placeholders

def getColors():
    return colors