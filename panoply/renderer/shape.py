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


def plotLow(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    
    D = (2 * dy) - dx
    y = y0

    points = []

    for x in range(x0, x1 + 1):
        points.append((x, y))
        if D > 0:
            y = y + yi
            D = D + (2 * (dy - dx))
        else:
            D = D + 2 * dy

    return points

def plotHigh(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    
    D = (2 * dx) - dy
    x = x0

    points = []

    for y in range(y0, y1 + 1):
        points.append((x, y))
        if D > 0:
            x = x + xi
            D = D + (2 * (dx - dy))
        else:
            D = D + 2 * dx

    return points


def line(canvas, x0, y0, x1, y1, color):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            points = plotLow(x1, y1, x0, y0)
        else:
            points = plotLow(x0, y0, x1, y1)
    else:
        if y0 > y1:
            points = plotHigh(x1, y1, x0, y0)
        else:
            points = plotHigh(x0, y0, x1, y1)

    for i in points:
        canvas.SetPixel(i[0], i[1], color[0], color[1], color[2])

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
