import sys


def run_on_windows(func):
    def wrapper():
        a = func()
        a = a[:3]
        if a == 'win':
            print('Функция работает только под Windows')
        else:
            return None
    return wrapper

def run_on_linux(func):
    def wrapper():
        a = func()
        a = a[:3]
        if a == 'lin':
            print('Функция работает только под Linux')
        else:
            return None
    return wrapper

def run_on_macos(func):
    def wrapper():
        a = func()
        a = a[:3]
        if a == 'mac':
            print('Функция работает только под Macos')
        else:
            return None
    return wrapper

@run_on_macos
def sys_definition():
    a = sys.platform
    return a


sys_definition()
