import renderer
from renderer import text, shape
import config
import matrix
import data

import time
import sys

def test():
    try:
        print("Press CTRL+C to exit.")
        # Initialise a canvas
        offscreen_canvas = matrix.device.CreateFrameCanvas()

        while True:
            # Clear the canvas for the new frame
            offscreen_canvas.Clear()
            # Loop for every horizontal line in list
            for hline in config.HORIZONTAL_LINES:
                color = renderer.getColorTuple(hline[3])
                offscreen_canvas = shape.horizontalLine(offscreen_canvas, hline[0], hline[1], hline[2], color)

            # Loop for every vertical line in list
            for vline in config.VERTICAL_LINES:
                color = renderer.getColorTuple(vline[3])
                offscreen_canvas = shape.verticalLine(offscreen_canvas, vline[0], vline[1], vline[2], color)

            # Loop for every rectangle in list
            for rectangle in config.RECTANGLES:
                color = renderer.getColorTuple(rectangle[4])
                offscreen_canvas = shape.rectangle(offscreen_canvas, rectangle[0], rectangle[1], rectangle[2], rectangle[3], color)

            # Loop for every text in list
            for textentity, values in config.LARGE_TEXT_ELEMENTS.items():
                textresult = textentity
                # Attempt to replace placeholders
                for dataname, dataresult in data.getPlaceholders().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)
                color = renderer.getColorTuple(values[2])
                # Add message to display
                offscreen_canvas = text.largeFont(offscreen_canvas, values[0], values[1], color, textresult)

            # Loop for every text in list
            for textentity, values in config.SMALL_TEXT_ELEMENTS.items():
                textresult = textentity
                    # Attempt to replace placeholders
                for dataname, dataresult in data.getPlaceholders().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)
                color = renderer.getColorTuple(values[2])
                # Add message to display
                offscreen_canvas = text.smallFont(offscreen_canvas, values[0], values[1], color, textresult)

            # Loop for every text in list
            for textentity, values in config.TINY_TEXT_ELEMENTS.items():
                textresult = textentity
                    # Attempt to replace placeholders
                for dataname, dataresult in data.getPlaceholders().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)
                color = renderer.getColorTuple(values[2])
                # Add message to displayt
                offscreen_canvas = text.tinyFont(offscreen_canvas, values[0], values[1], color, textresult)
            
            offscreen_canvas = matrix.device.SwapOnVSync(offscreen_canvas)
            time.sleep(config.DISPLAY_REFRESH_RATE)

    except KeyboardInterrupt:
        print("Stopping...")
        sys.exit(0)
