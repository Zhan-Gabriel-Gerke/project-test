from sqlite3 import *
from sqlite3 import Error
def create_conection(path):
    connection = None
    try:
        connection = connect(path)
        print('Uhendus on edukalt tehtud')
    except Error as e:
        print(f'Tekkis viga"{e}"')
    return connection
conn=create_conection(r"C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\DB\AppData\data.db")
def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print('Tabel on loodud')
    except Error as e:
        print(f'Viga "{e}" tabeli loomisega')

create_user_table = """
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
nationality TEXT
);
"""
# execute_query(conn, create_user_table)
inser_into_tabel = """
INSERT INTO users(name, age, gender, nationality)
VALUES('Zhan59', 59, 'TEXT-TEXT', 'TUDA_SJUDA_MILIONER')
"""
execute_query(conn, inser_into_tabel)
def execute_quert_read(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'Viga "{e}"')
select_users = "SELECT * FROM users"
users = execute_quert_read(conn, select_users)
for user in users:
    print(user)
