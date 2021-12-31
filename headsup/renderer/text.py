import matrix
from rgbmatrix import graphics

def draw(canvas, x, y, color, text):
    font = graphics.Font()
    font.LoadFont("../fonts/PixeloidMono.bdf")
    textColor = graphics.Color(color[0], color[1], color[2])

    graphics.DrawText(canvas, font, x, y, textColor, text)
    
    return canvas
