def is_palindrome(s):
    s = s.lower()
    l1 = s.split()
    l2 = ''.join(l1)
    s2 = list(l2)
    s3 = s2[:]
    s3.reverse()
    m = len(s2)
    for i in range(m):
        if s2[i] == s3[i]:
            if i == m-1:
                print(True)
        else:
            print(False)
            break
    i = i + 1
s = 'Я бы изменил мир, но бог не дает исходники'
print(is_palindrome(s))
s = 'Сел в озере березов лес'
print(is_palindrome(s))
