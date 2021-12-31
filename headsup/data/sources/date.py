from datetime import datetime
import config

def getTime():
    now = datetime.now()

    return now.strftime(config.DATE_FORMAT)