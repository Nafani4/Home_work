from collections import namedtuple

def return_namedtuple(*names):
    def decorator(func):
        def wrapper(*digits):
            a = func(*digits)
            if isinstance(a, tuple):
                named_tuple = namedtuple('named_tuple', names)
                return named_tuple(*a)
        return wrapper
    return decorator

@return_namedtuple('one', 'two')
def func():
    return 1, 2
@return_namedtuple('one', 'two', 'three')
def func():
    return 1, 2, 3
