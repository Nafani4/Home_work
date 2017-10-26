from random import *
field = [['-' for x in range(10)] for y in range(10)]

def valid(field, row, col):
    pass


def print_field(field):
    for x in field:
        print(' '.join(x))
#
def test(field):
#    dots = []
    row = choice(range(10))
    col = choice(range(10))
#    dot = field[row][col]
    field[row][col] = 'x'
#    print(print_field(field))
    new_1 = 50
    while new_1 not in field:
        if col+1==0 and col-1==9:
            break
        if row + 1==0 and row - 1==9 :
            break
        znacheniya_1 = [(col+1),(col-1)]
        znacheniya = [(row-1), (row+1)]
        row_1 = choice(znacheniya)
        col_1 = choice(znacheniya_1)
        new = [row_1, col_1]
        new_1 = choice(new)
        try:
            if col_1 == new_1:
                field[row][col_1] = 'x'
                ship_2_2 = field[row][col_1]
                break
            else:
                field[row_1][col] = 'x'
                ship_2_2 = field[row_1][col]
                break
        except IndexError:
            continue

def shoot(a,b):
    a = int(input())
    b = int(input())
    if a ==

    print(print_field(field))
test(field)