from renderer import text, shape
import config
import matrix
import data

import time
import sys

def test():
    try:
        print("Press CTRL+C to exit.")
        while True:
            offscreen_canvas = matrix.device.CreateFrameCanvas()

            for hline in config.HORIZONTAL_LINES:
                offscreen_canvas = shape.horizontalLine(offscreen_canvas, hline[0], hline[1], hline[2], hline[3])

            for vline in config.VERTICAL_LINES:
                offscreen_canvas = shape.verticalLine(offscreen_canvas, vline[0], vline[1], vline[2], vline[3])

            for rectangle in config.RECTANGLES:
                offscreen_canvas = shape.rectangle(offscreen_canvas, rectangle[0], rectangle[1], rectangle[2], rectangle[3], rectangle[4])

            for textentity, values in config.LARGE_TEXT_ELEMENTS.items():
                textresult = textentity
                for dataname, dataresult in data.getData().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)

                offscreen_canvas = text.largeFont(offscreen_canvas, values[0], values[1], values[2], textresult)

            for textentity, values in config.SMALL_TEXT_ELEMENTS.items():
                textresult = textentity
                for dataname, dataresult in data.getData().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)

                offscreen_canvas = text.smallFont(offscreen_canvas, values[0], values[1], values[2], textresult)

            for textentity, values in config.TINY_TEXT_ELEMENTS.items():
                textresult = textentity
                for dataname, dataresult in data.getData().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)

                offscreen_canvas = text.tinyFont(offscreen_canvas, values[0], values[1], values[2], textresult)

            time.sleep(config.DISPLAY_REFRESH_RATE)
            offscreen_canvas = matrix.device.SwapOnVSync(offscreen_canvas)
    except KeyboardInterrupt:
        print("Stopping...")
        sys.exit(0)