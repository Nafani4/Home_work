"""
SQL - Standart Query Language
- DDL - Data Definition Language
    (CREATE TABLE)
- DML - Data Manipulation Language
    (SELECT, INSERT, UPDATE, DELETE)

СУБД - Система управления базами данных
Primary Key (Первичный ключ)
    Уникальный идентификатор
    Может быть int, может быть str
    Может быть составной (суррогатный)
Foreign Key (Внешний ключ)

Алгоритм работы с БД:
1. Установка соединения .connect()
2. Создание объекта курсора conn.cursor()
3. Выполнение SQL-запроса(ов) cursor.execute()
4. Если запрос изменяет данные/структуру
    4.1 зафиксировать изменения conn.commit()
4. Если запрос на выборку (получение) данных
    4.1 разобрать данные (fetch*)
"""

# SQLite3

import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('users.sqlite')
cursor = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

cursor.execute(sql)

conn.commit()


sql = """
    INSERT INTO user (
        firstname, lastname
    ) VALUES (
        ?, ?
    )
"""

cursor.execute(sql, ('Вася', 'Пупкин'))
conn.commit()


sql = """
    SELECT
        id, firstname, lastname, created
    FROM
        user
"""

cursor.execute(sql)
users = cursor.fetchall()
print(users)

conn.close()


# Используя контекстный мендежер
# все можно сократить

with sqlite3.connect('users.sqlite') as conn:
    cursor = conn.execute(sql)
    users = cursor.fetchall()
    print(users)







