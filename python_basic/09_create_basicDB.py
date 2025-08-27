import sqlite3

conn = sqlite3.connect('Hello.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER                
)
''')

cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Me', 19))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Her', 18))

conn.commit()

cursor.close()
conn.close()

print(f"[+] All Done!")