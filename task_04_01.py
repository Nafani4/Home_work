n = int(input())
m = int(input())
with open('data.txt') as data:
    str1 = ""
    str2 = ""
    str3 = ""
    t = len(data.read())
    data.seek(0)
    for s1 in range(0, t):
        s = data.read(1)
        if s == ' ':
            chislo = int(str1)
            if chislo % n == 0:
                str3 = str3 + str(chislo) + ' '
            str2 = str2 + str(chislo ** m) + ' '
            str1 = ""
#        elif s == t:
#            if chislo % n == 0:
#                str3 = str3 + str(chislo)
#            str2 = str2 + str(chislo ** m)
        else:
            str1 = str1 + s
    s1 += s1
    chislo = int(str1)
    if chislo % n == 0:
        str3 = str3 + str(chislo)
    str2 = str2 + str(chislo ** m)

with open('out-1.txt', 'w') as out_1:
    out_1.write(str3)

with open('out-2.txt', 'w') as out_2:
    out_2.write(str2)