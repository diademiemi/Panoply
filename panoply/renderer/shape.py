# canvas    - canvas to modify
# x         - x starting coordinate
# y         - y starting coordinate
# len       - length of the line
# color     - tuple of RGB colors

def verticalLine(canvas, x, y, len, color):
    # Draw pixel for every pixel in length
    for i in range(len):
        canvas.SetPixel(x, y + i, color[0], color[1], color[2])
    
    return canvas

def horizontalLine(canvas, x, y, len, color):
    # Draw pixel for every pixel in length
    for i in range(len):
        canvas.SetPixel(x + i, y, color[0], color[1], color[2])
    
    return canvas

# canvas    - canvas to modify
# x         - x starting coordinate
# y         - y starting coordinate
# lenx      - rectangle width
# leny      - rectangle height
# color     - tuple of RGB colors

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
