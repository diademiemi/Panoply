def verticalLine(canvas, x, y, len, color):
    for i in range(len):
        canvas.SetPixel(x, y + i, color[0], color[1], color[2])
    
    return canvas

def horizontalLine(canvas, x, y, len, color):
    for i in range(len):
        canvas.SetPixel(x + i, y, color[0], color[1], color[2])
    
    return canvas

def rectangle(canvas, x, y, lenx, leny, color):
    # Top x line
    for i in range(lenx):
        canvas.SetPixel(x + i, y, color[0], color[1], color[2])
    # Left y line
    for i in range(leny):
        canvas.SetPixel(x, y + i, color[0], color[1], color[2])
    # Bottom x line
    for i in range(lenx):
        canvas.SetPixel(x + i, y + leny - 1, color[0], color[1], color[2])
    # Right y line
    for i in range(leny):
        canvas.SetPixel(x + lenx - 1, y + i, color[0], color[1], color[2])

    return canvas