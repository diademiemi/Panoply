from renderer import text, line, rectangle
import config
import matrix
import data

import time
import sys

def getColorTuple(color):
    if isinstance(color, str):
        tuple = data.getColors()[color]
    else:
        tuple = color
    
    return tuple


def start():
    try:
        print("Press CTRL+C to exit.")
        # Initialise a canvas
        offscreen_canvas = matrix.device.CreateFrameCanvas()

        while True:
            # Clear the canvas for the new frame
            offscreen_canvas.Clear()

            # Loop for every rectangle in list
            for rect in config.RECTANGLES:
                color = getColorTuple(rect[4])
                offscreen_canvas = rectangle.draw(offscreen_canvas, rect[0], rect[1], rect[2], rect[3], color)

            # Loop for every line in list
            for ln in config.LINES:
                color = getColorTuple(ln[4])
                offscreen_canvas = line.draw(offscreen_canvas, ln[0], ln[1], ln[2], ln[3], color)

            # Loop for every text in list
            for textentity, values in config.LARGE_TEXT_ELEMENTS.items():
                textresult = textentity
                # Attempt to replace placeholders
                for dataname, dataresult in data.getPlaceholders().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)
                color = getColorTuple(values[2])
                # Add message to display
                offscreen_canvas = text.largeFont(offscreen_canvas, values[0], values[1], color, textresult)

            # Loop for every text in list
            for textentity, values in config.SMALL_TEXT_ELEMENTS.items():
                textresult = textentity
                    # Attempt to replace placeholders
                for dataname, dataresult in data.getPlaceholders().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)
                color = getColorTuple(values[2])
                # Add message to display
                offscreen_canvas = text.smallFont(offscreen_canvas, values[0], values[1], color, textresult)

            # Loop for every text in list
            for textentity, values in config.TINY_TEXT_ELEMENTS.items():
                textresult = textentity
                    # Attempt to replace placeholders
                for dataname, dataresult in data.getPlaceholders().items():
                    if "%{}%".format(dataname) in textresult:
                        textresult = textresult.replace("%{}%".format(dataname), dataresult)
                color = getColorTuple(values[2])
                # Add message to displayt
                offscreen_canvas = text.tinyFont(offscreen_canvas, values[0], values[1], color, textresult)
            
            offscreen_canvas = matrix.device.SwapOnVSync(offscreen_canvas)
            time.sleep(config.DISPLAY_REFRESH_RATE)

    except KeyboardInterrupt:
        print("Stopping...")
        sys.exit(0)
