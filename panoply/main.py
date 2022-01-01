import matrix
import data
from renderer import display
import threading

global t

t = threading.Condition()

matrix.init()

class DisplayThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        display.test()

data.start()

TDisplay = DisplayThread("DisplayThread")

TDisplay.start()

TDisplay.join()

