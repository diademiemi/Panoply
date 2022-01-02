import matrix
import data
from renderer import display
import threading

global t

t = threading.Condition()

matrix.init()

# Create a class for the display thread
class DisplayThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        display.test()

# Collect data, once these have ran it will be scheduled periodically
data.start()

# Launch display in a separate thread
TDisplay = DisplayThread("DisplayThread")
TDisplay.start()
TDisplay.join()
