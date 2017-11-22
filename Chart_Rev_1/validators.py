from string import ascii_letters, digits, punctuation

def name_validator(value):
    valid_values = list(ascii_letters + digits)
    value = list(value)
    value = list(filter(lambda x: x not in valid_values, value))
    if value != []:
        return False
    return True

def pass_validator(value):
    valid_values = list(ascii_letters + digits + punctuation)
    value = list(value)
    value = list(filter(lambda x: x not in valid_values, value))
    if value != []:
        return False
    return True
#
#
# class ValidatorException(Exception):
#     pass
#
# class Validator(metaclass=ABCMeta):
#     methods = {}
#
#     @abstractmethod
#     def validate(self, value):
#         pass
#
#     @classmethod
#     def add_type(cls, name, klass):
#         if not name:
#             raise ValidatorException('Валидатору необходимо присвоить имя!')
#         if not issubclass(klass, Validator):
#             raise ValidatorException('Класс "{}" не является валидатором!'.format(klass))
#         cls.methods[name] = klass
#
#     @classmethod
#     def get_instance(cls, name):
#         klass = cls.methods.get(name)
#         if klass is None:
#             raise ValidatorException('Валидатор с именем "{}" не найден'.format(name))
#         return klass()
#
#     @staticmethod
#     def choose_validator(type):
#         Validator.add_type()
#
#
# class PassValidator(Validator):
#     def validate(self, value):
#         valid_values = list(ascii_letters + digits + punctuation)
#         value = list(value)
#         value = list(filter(lambda x: x not in valid_values, value))
#         if value != []:
#             return False
#         return True
#
#
# class NameValidator(Validator):
#     def validate(self, value):
#         valid_values = list(ascii_letters + digits)
#         value = list(value)
#         value = list(filter(lambda x: x not in valid_values, value))
#         if value != []:
#             return False
#         return True
#
# # Validator.add_type('pass', PassValidator)
# # Validator.add_type('name', NameValidator)
#
# if __name__ == '__main__':
#     validator = Validator.get_instance('pass')
#     print(validator.validate('afasfwr90#|}{P?>*<M|#($)&!pp'))
#     validator = Validator.get_instance('name')
#     print(validator.validate('afasfwr90da)**'))