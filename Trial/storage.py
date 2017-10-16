
import sqlite3

conn = sqlite3.connect("storage.sqlite") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE calendar
                  (id text, task text, creat text)
               """)
albums = [('1', 'task', 'created')]

cursor.executemany("INSERT INTO calendar VALUES (?, ?, ?)", albums)
conn.commit()

sql = "SELECT * FROM calendar WHERE id=?"
id = 2
sql = "UPDATE calendar WHERE id=?"
cursor.execute(sql, [""])
print(cursor.fetchall())
