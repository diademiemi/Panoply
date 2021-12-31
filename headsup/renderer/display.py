from renderer import text
import matrix

import time
import sys

def test():
    try:
        print("Press CTRL+C to exit.")
        while True:
            offscreen_canvas = text.draw(10, 20, (200, 200, 200), "Testing!")
            for x in range(64):
                offscreen_canvas.SetPixel(x, 32, 200, 0, 0)
            time.sleep(0.5)
            offscreen_canvas = matrix.device.SwapOnVSync(offscreen_canvas)
    except KeyboardInterrupt:
        print("Stopping...")
        sys.exit(0)