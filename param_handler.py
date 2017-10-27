from abc import *

class ParamHandler(metaclass=ABCMeta):
    types = {}
    def __init__(self, source):
        self.source = source
    #     self.param = {}
    #
    # def add_param(self, key, value):
    #     self.param[key] = value

    @abstractmethod
    def read_file(self):
        """Реализация чтения файла"""

    @abstractmethod
    def write_in_file(self):
        pass


    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException (
                'Class {} is not ParamHandler'.format(klass)
            )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        ext = source.split('.')[-1]
        klass = cls.types.get(ext)
        print(klass)
        # if klass is None:
        #     raise ParamHandlerException(
        #         'Type {} is not found'.format(ext)
        #         )
        return klass(source, *args, **kwargs)


class TxtParamHandler(ParamHandler):
    # def __init__(self, source):
    #     super().__init__(source)
    #     self.source = source
    def read_file(self):
        with open(self.source, 'r') as r:
            content = r.read()
            return content
    def write_in_file(self):
        with open(self.source, 'a') as f:
            f.write('Что-то дописалось')

class PickleParamHandler(ParamHandler):
    def read(self):
        """чтение из файла"""
    def write(self):
        """чтение в файл"""

ParamHandler.add_type('txt', TxtParamHandler)
chitaem = ParamHandler.get_instance('C:\Study\Home_work\data.txt')
chitaem.write_in_file()
print(chitaem)
print(chitaem.read_file())