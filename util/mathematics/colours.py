def rgb_to_hex(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)

def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value - minimum) / (maximum - minimum)
    b = int(max(0, 255 * (1 - ratio)))
    r = int(max(0, 255 * (ratio - 1)))
    g = 255 - b - r
    return r, g, b

def grayscale_rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = (value - minimum) / (maximum - minimum)
    return (255 * ratio), (255 * ratio), (255 * ratio)

def island_rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = (value - minimum) / (maximum - minimum)

    if ratio < 0.1:
        return 1, 101, 199
    elif ratio < 0.2:
        return 1, 146, 199
    elif ratio < 0.3:
        return 241, 222, 119
    elif ratio < 0.4:
        return 155, 188, 47
    elif ratio < 0.5:
        return 80, 142, 7
    elif ratio < 0.6:
        return 26, 109, 3
    elif ratio < 0.7:
        return 48, 142, 92
    elif ratio < 0.8:
        return 169, 170, 126
    elif ratio < 0.9:
        return 135, 107, 44
    elif ratio < 0.95:
        return 125, 125, 125
    elif ratio < 0.99:
        return 75, 75, 75
    elif ratio == 1.0:
        return 255, 255, 255
    else:
        return 255, 255, 255
