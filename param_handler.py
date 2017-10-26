from abc import *

class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.sorce = source
        self.param = {}

    def add_param(self, key, value):
        self.param[key] = value

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_in_file(self):
        pass

    @staticmethod
    def get_instance(source):
        ext = 'source'.split('.')[-1]
        if ext == 'txt':
            return TxtParamHandler(source)


class TxtParamHandler(ParamHandler):
    def read_file(self):
        with open('source', 'r') as r:
            content = r.read()
            print(content)
    def write_in_file(self):
        with open('source', 'a') as f:
            f.write('Что-то дописалось')

class PickleParamHandler(ParamHandler):
    def read(self):
        """чтение из файла"""
    def write(self):
        """чтение в файл"""

chitaem = ParamHandler.get_instance('C:\Study\Home_work\data.txt')
print(chitaem.read_file())