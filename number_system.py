from string import digits, ascii_letters

valid_values = list(digits + ascii_letters[26:32])


def convert(number, radix):
    number = int(number)
    radix = int(radix)
    lst = []
    while number > 0:
        result = valid_values[number % radix]
        lst.insert(0, result)
        number = number // radix
    lst = ''.join(lst)
    return lst


def inverse(number, radix):
    radix = int(radix)
    result = 0
    for p, i in enumerate(reversed(number)):
        n = valid_values.index(i)
        result += n * radix ** p

    return result


def dec2bin(number):
    result = convert(number, 2)
    return result


def dec2oct(number):
    result = convert(number, 8)
    return result


def dec2hex(number):
    result = convert(number, 16)
    return result


def bin2dec(number):
    result = inverse(number, 2)
    return result


def oct2dec(number):
    result = inverse(number, 8)
    return result


def hex2dec(number):
    result = inverse(number, 16)
    return result


if (__name__=="__main__"):
    print(dec2bin(250))
    print(dec2oct(250))
    print(dec2hex(250))
    print(bin2dec('1010011010'))
    print(oct2dec('755'))
    print(hex2dec('ABCDEF'))

