import matrix
from rgbmatrix import graphics

def draw(x, y, color, text):
    offscreen_canvas = matrix.device.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("../fonts/PixeloidMono.bdf")
    textColor = graphics.Color(color[0], color[1], color[2])

    graphics.DrawText(offscreen_canvas, font, x, y, textColor, text)
    
    return offscreen_canvas
