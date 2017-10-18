from string import digits, ascii_letters

valid_values = list(digits + ascii_letters)
radix = len(valid_values)


def convert(number):
    result = []

    while number:
        result.insert(0, valid_values[number % radix])
        number //= radix

    return ''.join(result)


def inverse(number):
    result = 0

    for p, i in enumerate(reversed(number)):
        n = valid_values.index(i)
        result += n * radix ** p

    return result




