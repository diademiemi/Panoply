import config
import data

def getColorTuple(color):
    if isinstance(color, str):
        tuple = data.getColors()[color]
    else:
        tuple = color
    
    return tuple
