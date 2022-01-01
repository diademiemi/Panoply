import config

from rgbmatrix import graphics

# canvas    - canvas to modify
# x         - x starting coordinate
# y         - y starting coordinate
# color     - tuple of RGB colours
# text      - text to display

def largeFont(canvas, x, y, color, text):
    font = graphics.Font()
    font.LoadFont(config.LARGE_FONT)
    textColor = graphics.Color(color[0], color[1], color[2])

    graphics.DrawText(canvas, font, x, y, textColor, text)
    
    return canvas

def smallFont(canvas, x, y, color, text):
    font = graphics.Font()
    font.LoadFont(config.SMALL_FONT)
    textColor = graphics.Color(color[0], color[1], color[2])

    graphics.DrawText(canvas, font, x, y, textColor, text)
    
    return canvas

def tinyFont(canvas, x, y, color, text):
    font = graphics.Font()
    font.LoadFont(config.TINY_FONT)
    textColor = graphics.Color(color[0], color[1], color[2])

    graphics.DrawText(canvas, font, x, y, textColor, text)
    
    return canvas
