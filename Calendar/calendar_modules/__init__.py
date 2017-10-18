import os.path as Path
import sys

from calendar_modules import storage

get_connection = lambda : storage.connect('calendar.sqlite')


def action_find_all_tasks():
    """Вывести все задачи"""
    with get_connection() as conn:
        rows = storage.find_all_tasks(conn)

    template = '{row[id]} - {row[task]} - {row[status]} - {row[created]}'

    for row in rows:
        print(template.format(row=row))


def action_add_task():
    """Добавить задачу"""
    task = input('\nВведите задачу: ')
    if task:
        with get_connection() as conn:
            add_task = storage.add_task(conn, task)

        print('Была добавлена следущая задача: {}'.format(task))


def action_edit_task():
    pk = input('\nВведите id задачи: ')
    if pk:
        with get_connection() as conn:
            row = storage.find_task_by_pk(conn, pk)
        if row:
            task = input('\nОбновите задачу: ')
            with get_connection() as conn:
                edited_task = storage.edit_task(conn, task, pk)
            print('\nЗадача id {} изменена'.format(pk))
        else:
            print('Задача с id {} не существует'.format(pk))


def action_finish_task():
    pk = input('\nВведите id задачи: ')
    if pk:
        with get_connection() as conn:
            row = storage.find_task_by_pk(conn, pk)
        if row:
            status = 'finished'
            with get_connection() as conn:
                edit_status = storage.edit_status(conn, status, pk)
            print('\nЗадача id {} завершена'.format(pk))
        else:
            print('\nЗадача с id {} не существует'.format(pk))


def action_repeat_task():
    pk = input('\nВведите id задачи: ')
    if pk:
        with get_connection() as conn:
            row = storage.find_task_by_pk(conn, pk)
        if row:
            status = 'in progress'
            with get_connection() as conn:
                edit_status = storage.edit_status(conn, status, pk)
                print('\nЗадача id {} начата заново'.format(pk))

        else:
            print('Задача с id {} не существует'.format(pk))


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
        '3': action_edit_task,
        '4': action_finish_task,
        '5': action_repeat_task,
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
