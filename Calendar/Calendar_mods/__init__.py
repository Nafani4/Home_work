import sys
import os.path as Path
import datatime
from calendar_mods import storage


get_connection = lambda: storage.connect('storage.sqlite')


def action_add_task():
    #Добавить задачу
    task_name = input('\nВведите задачу: ')
    task_started_time = input('\nВведите время начала задачи в формате dd.mm.yyyy: ')
    task_ended_time = input('\nВведите время завершения задачи в формате dd.mm.yyyy: ')
    task_created = datetime.today()
#    if not task_name and task_started_time and task_ended_time:
#        return

    with get_connection as conn:
        task_name = storage.add_name(conn, task_name)
    print('Имя задачи: {}'.format(task_name))
    with get_connection as conn:
        task_started_time = storage.task_started_time(conn, task_started_time)
    print('Время начала: {}'.format(task_started_time))
    with get_connection as conn:
        task_ended_time = storage.task_ended_time(conn, task_ended_time)
    print('Время окончания: {}'.format(task_ended_time))
    with get_connection as conn:
        task_created = storage.task_created(conn, task_created)
    print('Файл создан: {}'.format(task_created))



def action_print_tasks():
    """Вывести все задачи на экран"""
    with get_connection() as conn:
        rows = storage.print_tasks(conn)

    template = '{row[id]} - {row[task_name]} - {row[task_status]}'

    for row in rows:
        print(template.format(row=row))


def action_modified_task():
   
    with get_connection() as conn:
        storage.add_modified_task(conn)


def action_show_menu():

    print("""Ежедневник. Выберите действие

    1. Вывести список задач
    2. Добавить задачу
    3. Отредактировать задачу
    4. Завершить задачу
    5. Начать задачу сначала
    m. Меню
    q. Выход""")


def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
        )

    with get_connection as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': action_print_tasks,
        '2': action_add_task,
        '3': action_modified_task,
        '4': action_end_task,
        '5': action_repeat_task,
        'm': action_show_menu,
        'q': action_exit
        }

    action_show_menu()

    while True:
        cmd = input('\nВведите команду')
        action = actions.get(cmd) 
        if action:
            action()
        else:
            print('Неизвестная команда')


def action_exit():
    sys.exit(0)



