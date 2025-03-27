import sqlite3
import tkinter as tk
from tkinter import messagebox
def opendb():
    global curs, conn
    conn = sqlite3.connect(r'C:\Users\zange\source\repos\Zhan-Gabriel-Gerke\project-test\FinalWork\AppData\data.db')
    curs = conn.cursor()
def create_custom_table(Username):
    opendb()
    sql = f""" CREATE TABLE IF NOT EXISTS {Username}(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserNameOrEmail VARCHAR(30),
    Password VARCHAR(30),
    Link TEXT,
    Notes TEXT);"""
    curs.execute(sql)
def select_users():
    opendb()
    try:
        #sql = 
        #curs.execute(sql)
        #conn.commit()
        pass
    except sqlite3.Error as e:
        tk.messagebox.showerror("showerror", e)
def insert_data(UserName, Phone, Email, Password):
    opendb()
    try:
        sql = f"""INSERT INTO users (UserName, Phone, Email, Password)
        VALUES('{UserName}', '{Phone}', '{Email}', '{Password}')"""
        curs.execute(sql)
        conn.commit()
        create_custom_table(UserName)
        return True
    except sqlite3.Error as e:
        tk.messagebox.showerror("showerror def insert_data", e)
    close()
def select_data():
    curs.execute("SELECT * FROM users")
    return curs.fetchall()
def close():
    conn.close()
def create_new_list():
    opendb()
    curs.execute("""CREATE TABLE IF NOT EXISTS users
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserName VARCHAR(30),
    Phone TEXT,
    Email VARCHAR(30) UNIQUE,
    Password TEXT);""")
    close()
def select_password(UserName):
    opendb()
    if len(UserName) > 5:
        try:
            sql = f"""SELECT Password from users
            Where UserName = '{UserName}';
            """
            curs.execute(sql)
            pswd = curs.fetchall()
            pswd = pswd[0]
            lenpswd = len(pswd)
            pswd = pswd[lenpswd - 2]# Тут можно спросить
            return pswd
        except sqlite3.Error as e:
            tk.messagebox.showerror("show error", e)
        close()
#insert_data("Zhan", "Gabriel", "1234567890", "zhan@tthk.ee", "securepassword")
# data = select_data()
# print(data)
