from rgbmatrix import graphics

def largeFont(canvas, x, y, color, text):
    font = graphics.Font()
    font.LoadFont("../fonts/PixeloidMono.bdf")
    textColor = graphics.Color(color[0], color[1], color[2])

    graphics.DrawText(canvas, font, x, y, textColor, text)
    
    return canvas

def smallFont(canvas, x, y, color, text):
    font = graphics.Font()
    font.LoadFont("../fonts/Small-5x7.bdf")
    textColor = graphics.Color(color[0], color[1], color[2])

    graphics.DrawText(canvas, font, x, y, textColor, text)
    
    return canvas

def tinyFont(canvas, x, y, color, text):
    font = graphics.Font()
    font.LoadFont("../fonts/Tiny-4x6.bdf")
    textColor = graphics.Color(color[0], color[1], color[2])

    graphics.DrawText(canvas, font, x, y, textColor, text)
    
    return canvas