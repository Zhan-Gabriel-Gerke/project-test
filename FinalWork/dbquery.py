import sqlite3
conn = sqlite3.connect('users.db')
curs = conn.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS users
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR(30),
SurName VARCHAR(30),
Phone TEXT,
Email VARCHAR(30),
Password TEXT);""")
def insert_data(Name, SurName, Phone, Email, Password):
    curs.execute(
        "INSERT INTO users (Name, SurName, Phone, Email, Password) VALUES(?, ?, ?, ?, ?)",
        (Name, SurName, Phone, Email, Password)
    )
    conn.commit()
def select_data():
    curs.execute("SELECT * FROM users")
    return curs.fetchall()
def close():
    conn.close()
insert_data("Zhan", "Gabriel", "1234567890", "zhan@tthk.ee", "securepassword")
data = select_data()
print(data)
close()