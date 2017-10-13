def iz_2_v_10():
    d = int(len(str1))
    a = list(str1)
    c = 0
    for i in a:
        i = int(i)
        c = c + i*(2**(d-1))
        d = d - 1
    return c
str1 = "1010011010"
if (__name__=="__main__"):
    print(iz_2_v_10(), '\n')


def iz_10_v_2():
    lst1 = []
    a2 = int(a1)
    d1 = a2 % 2
    d2 = a2 // 2
    lst1.append(str(d1))
    while d2 > 0:
        d1 = d2 % 2
        d3 = str(d1)
        lst1.append(str(d1))
        d2 = d2 // 2
    lst1.reverse()
    str2 = ''.join(lst1)
    return str2
a1 = 22

if (__name__=="__main__"):
    print(iz_10_v_2())




