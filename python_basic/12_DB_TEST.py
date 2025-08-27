import sqlite3

with sqlite3.connect('Hello.db') as conn:
    cursor = conn.cursor()
    cursor.execute('select * from users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)