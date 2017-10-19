import time


def pause(func):
    def wrapper():
        time.sleep(2)
        func()
    return wrapper


@pause
def func():
    print('Фунция выполняется с задержкой!')

func()
