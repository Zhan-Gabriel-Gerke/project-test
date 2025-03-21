import sqlite3
import tkinter as tk
from tkinter import messagebox
def opendb():
    global curs, conn
    conn = sqlite3.connect(r'C:\Users\zange\source\repos\Zhan-Gabriel-Gerke\project-test\FinalWork\AppData\data.db')
    curs = conn.cursor()
# curs.execute("""CREATE TABLE IF NOT EXISTS users
# (ID INTEGER PRIMARY KEY AUTOINCREMENT,
# Name VARCHAR(30),
# SurName VARCHAR(30),
# Phone TEXT,
# Email VARCHAR(30) UNIQUE,
# Password TEXT);""")
def insert_data(Name, SurName, Phone, Email, Password):
    opendb()
    try:
        curs.execute(
            "INSERT INTO users (Name, SurName, Phone, Email, Password) VALUES(?, ?, ?, ?, ?)",
            (str(Name), str(SurName), str(Phone), str(Email), str(Password))
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        tk.messagebox.showerror("showerror", e)
    close()
def select_data():
    curs.execute("SELECT * FROM users")
    return curs.fetchall()
def close():
    conn.close()
#insert_data("Zhan", "Gabriel", "1234567890", "zhan@tthk.ee", "securepassword")
# data = select_data()
# print(data) 