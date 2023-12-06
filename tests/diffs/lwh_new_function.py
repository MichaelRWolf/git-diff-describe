def fn(d1, d2, d3):
    value = d1 * d2 * d3
    return value


def surface_area(l, w, h):
    return sum([l * w, w * h, h * l]) * 2


def main():
    l = 3
    w = 4
    h = 5
    vol = fn(l, w, h)
    print
    vol
