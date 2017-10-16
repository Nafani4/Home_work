import os.path as Path
import sqlite3


SQL_SELECT_ALL = """
    SELECT
        id, task, created
    FROM
        calendar
"""

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_TASK_BY_CREATED = SQL_SELECT_ALL + " WHERE created=?"

SQL_SELECT_TASK_BY_TASK =  SQL_SELECT_ALL + " WHERE task=?"

SQL_INSERT_TASK = """
    INSERT INTO calendar (task) VALUES (?)
"""

SQL_UPDATE_TASK = """
    UPDATE calendar SET task=? WHERE id=?
"""


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())



def add_task(conn, task, domain=''):
    """сохраняет новую задачу"""
    with conn:

        cursor = conn.execute(SQL_INSERT_TASK, (task,))
        

def find_task_by_task(conn, task):

    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_TASK,
                              (task,))
        return cursor.fetchone()      


def update_task(conn, task, pk):
    """ обновить задачу"""
    with conn:
        conn.execute(SQL_UPDATE_TASK, (task, pk))


def find_all_tasks(conn):
    """Возвращает все URL-адреса из базы"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_task_by_pk(conn, pk):
    """Возвращает URL-адрес по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
        return cursor.fetchone()


def find_url_by_short(conn, short_url):
    """Возвращает URL-адрес по короткому URL-у"""
    short_url = short_url.rsplit('/', 1).pop()
    pk = inverse(short_url)
    return find_url_by_pk(conn, pk)










