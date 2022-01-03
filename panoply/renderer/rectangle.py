
def plot(x0, y0, x1, y1):
    points = []
    for i in range(x1 - x0):
        points.append((x0 + i, y0))
        points.append((x0 + i + 1, y0 + (y1 - y0)))
    for i in range(y1 - y0):
        points.append((x0, y0 + i + 1))
        points.append((x0 + (x1 - x0), y0 + i ))

    return points

# canvas    - canvas to modify
# x0        - x starting coordinate
# y0        - y starting coordinate
# x1        - x ending coordinate
# y1        - y ending coordinate
# color     - tuple of RGB colors
def draw(canvas, x0, y0, x1, y1, color):
    if y0 <= y1:
        if x0 < x1:
            points = plot(x0, y0, x1, y1)
        else:
            points = plot(x1, y0, x0, y1)
    else:
        if x0 < x1:
            points = plot(x0, y1, x1, y0)
        else:
            points = plot(x1, y1, x0, y0)

    for i in points:
        canvas.SetPixel(i[0], i[1], color[0], color[1], color[2])

    return canvas
