import os.path as Path
import sys

from url_calendar import storage

get_connection = lambda : storage.connect('calendar.sqlite')


def action_add_task():
    """Добавить URL-адрес"""
    task = input('\nВведите задачу: ')

    with get_connection() as conn:
        add_task = storage.add_task(conn, task)

    print('Задача добавлена: {}'.format(task))


def action_find_all_tasks():
    """Вывести все URL-адреса"""
    with get_connection() as conn:
        rows = storage.find_all_tasks(conn)

    template = '{row[id]} - {row[task]} - {row[created]}'

    for row in rows:
        print(template.format(row=row))


def action_show_menu():
    """Показать меню"""
    print("""
1. Вывести список задач
2. Добавить задачу
3. Редактировать задачу
4. Завершить задачу
5. Начать задачу сначала
m. Показать меню
q. Выйти""")


def action_exit():
    """Выйти из программы"""
    sys.exit(0)


def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)


    actions = {
        '1': action_find_all_tasks,
        '2': action_add_task,
#        '3': action_edit_task,
#        '4': finish_task,
#        '5': repeat_task,
        'm': action_show_menu,
        'q': action_exit
    }

    action_show_menu()

    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')
