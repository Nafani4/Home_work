from string import *

def validate(value):
    """Разбиваем на 2 части, которые проверяем отдельно"""
    razbivka = value.split('@')
    if len(razbivka) < 2 or razbivka[0] == '' or razbivka[-1] == '':
        return False
    domain = razbivka[1]
    damain = domain.split('.')
    if len(damain) < 2 or damain[0] == '' or damain[-1] == '':
        return False
    print(domain)
    return True

print(validate('in@fotecj-tv.tu'))
