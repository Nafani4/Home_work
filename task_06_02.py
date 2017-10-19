import time
from functools import wraps


def pause(delay):
    def decorator(func):
        @wraps(func)
        def wrapper():
            time.sleep(delay)
            return func()
        return wrapper
    return decorator

@pause(delay=2)
def func():
    print('Фунция выполняется с задержкой!')

func()