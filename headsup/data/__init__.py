import threading
from data.sources import date, homeassistant
import config

global allData

allData = {}

def start():
    web_data()
    local_data()
    
def web_data():
    allData["temp"] = homeassistant.getTemp()
    threading.Timer(config.WEB_REFRESH_INTERVAL, web_data).start()


def local_data():
    allData["time"] = date.getTime()
    allData["date"] = date.getDate()
    threading.Timer(config.LOCAL_REFRESH_INTERVAL, local_data).start()


def getTime():
    return allData["time"]
def getDate():
    return allData["date"]

def getTemp():
    return allData["temp"]