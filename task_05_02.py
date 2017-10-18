def get_quadrant_number(x, y):
    def chislo(x, y):
        if x > 0 and y > 0:
            a = 1
            return a
        elif x < 0 and y > 0:
            a = 2
            return a
        elif x < 0 and y < 0:
            a = 3
            return a
        elif x > 0 and y < 0:
            a = 4
            return a
    if chislo(x, y):
        print(a)
    else:
        try:
            raise ValueError
        except:
            print('ValueError')

if (__name__=="__main__"):
    print(get_quadrant_number(5, 1))
    print(get_quadrant_number(5, 1))
    print(get_quadrant_number(5, 1))
    print(get_quadrant_number(0, 1))
