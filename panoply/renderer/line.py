# canvas    - canvas to modify
# x0        - x starting coordinate
# y0        - y starting coordinate
# x1        - x ending coordinate
# y1        - y ending coordinate
# color     - tuple of RGB colors
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


def draw(canvas, x0, y0, x1, y1, color):
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