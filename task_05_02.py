def get_quadrant_number(x, y):
    if x == 0 or y == 0:
        raise ValueError
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

if __name__ == '__main__':
    get_quadrant_number(0, 0)
    get_quadrant_number(1, 2)
