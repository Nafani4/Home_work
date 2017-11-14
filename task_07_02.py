import random
from string import ascii_letters, digits, punctuation

def decorator(func):
    def wrapper(*args, **kwargs):
        return (''.join(next(func(*args, **kwargs))))
    return wrapper


@decorator
def password_generator(x):
    password_range = (ascii_letters + digits + punctuation)
    yield random.sample(password_range, x)

if __name__ == '__main__':
    print(password_generator(16))
