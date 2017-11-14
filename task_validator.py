from abc import *
from datetime import *


class ValidatorException(Exception):
    pass

class Validator(metaclass=ABCMeta):
    methods = {}

    @abstractmethod
    def validate(self):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Validator must have a name!')
        if not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))
        cls.methods[name] = klass

    @classmethod
    def get_instance(cls, name):
        klass = cls.methods.get(name)
        if klass is None:
            raise ValidatorException('Validator with name "{}" not found'.format(name))
        return klass()

class EMailValidator(Validator):
    def validate(self, value):
        razbivka = value.split('@')
        if len(razbivka) < 2 or razbivka[0] == '' or razbivka[-1] == '':
            return False
        domain = razbivka[1]
        domain = domain.split('.')
        if len(domain) < 2 or domain[0] == '' or domain[-1] == '':
            return False
        return True

class DateTimeValidator(Validator):
    def validate(self, value):
        allow_formats = [
            '%Y-%m-%d',
            '%Y-%m-%d %H:%M',
            '%Y-%m-%d %H:%M:%S',
            '%d.%m.%Y',
            '%d.%m.%Y %H:%M',
            '%d.%m.%Y %H:%M:%S',
            '%d/%m/%Y',
            '%d/%m/%Y %H:%M',
            '%d/%m/%Y %H:%M:%S'
]
        for i in allow_formats:
            try:
                datetime.strptime(value, i)
                return True
            except:
                continue
        return False

Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)

if __name__ == '__main__':
    validator = Validator.get_instance('email')
    print(validator.validate('info@itmo-it.org'))
    print(validator.validate('unknown'))

    validator = Validator.get_instance('datetime')
    print(validator.validate('1.9.2017'))
    print(validator.validate('01/09/2017'))
    print(validator.validate('2017-09-01 12:00:00'))