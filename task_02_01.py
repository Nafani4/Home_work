def is_palindrome(s):
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
s = 'я бы изменил мир, но бог не дает исходникя'
print(is_palindrome(s))
s = 'сел в озере березов лес'
print(is_palindrome(s))