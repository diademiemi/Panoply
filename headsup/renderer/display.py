from renderer import text
import matrix
import data

import time
import sys

def test():
    try:
        print("Press CTRL+C to exit.")
        while True:
            offscreen_canvas = matrix.device.CreateFrameCanvas()
            offscreen_canvas = text.draw(offscreen_canvas, 5, 10, (200, 200, 200), data.getTime())
            offscreen_canvas = text.draw(offscreen_canvas, 2, 40, (200, 200, 200), "It's {}c".format(data.getTemp()))
            for x in range(64):
                offscreen_canvas.SetPixel(x, 12, 200, 0, 0)
            time.sleep(0.5)
            offscreen_canvas = matrix.device.SwapOnVSync(offscreen_canvas)
    except KeyboardInterrupt:
        print("Stopping...")
        sys.exit(0)