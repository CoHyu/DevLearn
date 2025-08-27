import sqlite3

with sqlite3.connect('Hello.db') as conn:
    cursor = conn.cursor()
    name = input()
    cursor.execute("SELECT * FROM users WHERE name='%s'", (name))
    result = cursor.fetchone()
    print(result)