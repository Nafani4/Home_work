def is_palindrome(s):
    not_valid_values = list(' !@#$%^&*_+:?><!"№;%:?*_+,.')
    s = str(s).lower()
    s = list(s)
    s = list(filter(lambda x: x not in not_valid_values, s))
    if s != s[::-1]:
        return False
    return True


if __name__ == '__main__':
    print(is_palindrome(49094))
    print(is_palindrome('Я бы изменил мир, но бог не дает исходники'))
    print(is_palindrome('Сел в озере березов лес'))