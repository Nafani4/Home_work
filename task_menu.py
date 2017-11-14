from abc import *

class CommandException(Exception):
    pass

class Command(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def show_name(self):
        pass


class Menu(object):
    def __init__(self):
        self.menu = {}
    def add_command(self, name, klass):
        if not name:
            raise CommandException
        elif not issubclass(klass, Command):
            raise CommandException
        self.menu[name] = klass
    def show_menu(self):
        for i in self.menu:
            print(i,'', end='')
            self.menu[i]().show_name()
    def __iter__(self):
        self.iter = iter(self.menu)
        return self
    def __next__(self):
        a = next(self.iter)
        b = self.menu[a]
        return (a, b)
    def execute(self, name, *args, **kwargs):
        if not name in self.menu:
            raise CommandException
        self.menu[name](*args, **kwargs).execute()


class ShowTasks(Command):
    def execute(self):
        print('Все задачи показаны')
    def show_name(self):
        print('Вывести список задач')

class AddTask(Command):
    def execute(self):
        print('Задача добавлена')
    def show_name(self):
        print('Добавить задачу')

if __name__ == "__main__":
    lst = [ShowTasks, AddTask]
    menu = Menu()
    for i in range(0, len(lst)):
        menu.add_command(str(i), lst[i])
    menu.show_menu()
    menu.execute('1')