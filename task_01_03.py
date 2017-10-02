a = int(input())
b = int(input())
c = int(input())
if a < b:
    if a < c:
        if c < b:
            print(a, c, b, sep=', ')
        else:
            print(a, b, c, sep=', ')
    else:
        print(c, a, b, sep=', ')
else:
    if c < a:
        if c < b:
            print(c, b, a, sep=', ')
        else:
            print(b, c, a, sep=', ')
    else:
        print(b, a, c, sep=', ')