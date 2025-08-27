import sqlite3

while True:
    with sqlite3.connect('Hello.db') as conn:
        print(
'''
=======================
1. Insert data
2. Update data (age)
3. Delete data
4. Select data
5. Exit
=======================
'''
        )
        PF = input("Enter your performance:")
        cursor = conn.cursor()
        if PF == "1":
            name, age = input("Enter name and age:").split()
            try:
                cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", (name, age))
                cursor.execute('SELECT * FROM users WHERE name=?', (name,))
                row = cursor.fetchone()
                print(f"[+] Inserted :{row}")
            except Exception as e:
                print(f"[-] Insert failed: {e}")
        elif PF == "2":
            name, age = input("Enter name and age:").split()
            try:
                cursor.execute("UPDATE users SET age=? WHERE name=?", (age, name))
                cursor.execute('SELECT * FROM users WHERE name=?', (name,))
                row = cursor.fetchone()
                print(f"[+] Updated :{row}")
            except Exception as e:
                print(f"[-] Update failed: {e}")
        elif PF == "3":
            name = input("Enter name: ")
            try:
                cursor.execute("DELETE FROM users WHERE name=?", (name,))
                print(f"[+] Deleted user: {name}")
                cursor.execute('SELECT * FROM users')
                rows = cursor.fetchall()
                print("[+] Remaining users:")
                for row in rows:
                    print(row)
            except Exception as e:
                print(f"[-] Delete failed: {e}")
        elif PF == "4":
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        elif PF == "5":
            break