
def get_quadrant_number(x, y):
    try:
        if x == 0 or y == 0:
            raise ValueError
        elif x > 0:
            return 1 if y > 0 else 4
        elif x < 0:
            return 2 if y > 0 else 3
    except ValueError:
        print('ValueError')

if __name__ == '__main__':
    get_quadrant_number(0, 0)
    get_quadrant_number(1, 0)
    get_quadrant_number(-1, 1)
