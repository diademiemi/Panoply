import matrix
import data
import renderer
import threading

matrix.init()

# Create a class for the display thread
class DisplayThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        renderer.start()

# Collect data, once these have ran it will be scheduled periodically in a separate thread
data.start()

# Launch display in a separate thread
TDisplay = DisplayThread("DisplayThread")
TDisplay.start()
TDisplay.join()
