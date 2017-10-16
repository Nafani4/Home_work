import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT
        id, task_name,
        task_started_time, task_ended_time, 
        task_modified, task_created,
        task_status
    FROM
        calendar
"""

SQL_SELECT_TASK_BY_ID  = SQL_SELECT_ALL + " WHERE id=?"
SQL_SELECT_TASK_BY_TASK_NAME = SQL_SELECT_ALL + " WHERE task_name=?"
SQL_SELECT_TASK_BY_STARTED = SQL_SELECT_ALL + " WHERE task_started=?"
SQL_SELECT_TASK_BY_ENDED = SQL_SELECT_ALL + " WHERE task_ended=?"
SQL_SELECT_TASK_BY_CREATED = SQL_SELECT_ALL + " WHERE task_created=?"
SQL_SELECT_TASK_BY_MODIFIED = SQL_SELECT_ALL + " WHERE task_MODIFIED=?"

SQL_INCERT_NAME = """
    INCERT INTO calendar (task_name) VALUES (?)
    """

SQL_UPDATE_STARTED_TIME = """
    UPDATE calendar SET task_started WHERE id=?
    """

SQL_UPDATE_ENDED_TIME = """
    UPDATE calendar SET task_ended WHERE id=?
    """

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    # магия

    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())


def add_task(conn, task):
    pass
    #Добавляет новую задачу в базу


def add_modified_task(conn, task):
    pass
    #Изменяет задачу и обновляет её в базе


def add_repeat_task(conn, task_name):
    pass
    #Возвращает задачу по названию и начинает её заново.


def print_tasks(conn):
    pass
    #Возвращает все задачи из базы


def print_active_tasks(conn, status):
    pass
    #Возвращает все незавершённые задачи


def show_id(conn, task_name):
    pass
    #Возвращает номер задачи по названию




#def find_all_ended_tasks(conn, task_ended_time):
    #Возвращает все завершённые задачи


#def find_all_in_period(conn, task_started_time, task_ended_time):
    #Возвращает все задачи за определённый период
    

#def find_all_active_in_period(conn, task_started_time, task_ended_time):
    #Возвращает все активные задачи за определённый период


#def find_task_time(conn, task_ended):
    #Возвращает время начала и время до окончания задачи 
    #или время просрочки по названию задачи









