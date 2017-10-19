import random
from string import ascii_letters


def print_gen(a):
    print(''.join(next(a)))


def decorator(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        print_gen(a)
    return wrapper


@decorator
def password_generator(x):
    a = random.sample(ascii_letters, x)
    yield a


password_generator(16)
