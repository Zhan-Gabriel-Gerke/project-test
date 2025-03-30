from math import e
import sqlite3
import tkinter as tk
from tkinter import messagebox
#db_file = ['AppData/data.db']
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
def select_data_by_id(current_user, User_ID):
    opendb()
    try:
        sql = f"""SELECT * FROM {current_user}
        WHERE ID = {User_ID}"""
        curs.execute(sql)
        return curs.fetchall()
    except sqlite3.Error as e:
        tk.messagebox.showerror("showerror def selected_data_by_id", e)
def select_data(current_user):
    opendb()
    try:
        sql = f"SELECT * FROM {current_user}"
        curs.execute(sql)
        return curs.fetchall()
    except sqlite3.Error as e:
        tk.messagebox.showerror("showerror def select_data", e)
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
            if len(pswd) != 0:
                pswd = pswd[0]
                lenpswd = len(pswd)
                pswd = pswd[lenpswd - 2]# Тут можно спросить
                return pswd
        except ValueError as e:
            tk.messagebox.showerror("show error", e)
        close()
#insert_data("Zhan", "Gabriel", "1234567890", "zhan@tthk.ee", "securepassword")
# data = select_data()
# print(data)
def add_data_to_table(current_user,UserName, Password, Link, Notes):
    opendb()
    try:
        sql = (f"""INSERT INTO {current_user} (UserNameOrEmail, Password, Link, Notes)
        VALUES('{UserName}', '{Password}', '{Link}','{Notes}')""")
        curs.execute(sql)
        conn.commit()
        return True
    except sqlite3.Error as e:
        tk.messagebox.showerror("showerror def add_data_to_table", e)
def change_data(current_user, UserNameOrEmail, Password, Link, Notes, ID):
    print(current_user, UserNameOrEmail, Password, Link, Notes, ID)
    opendb()
    try:
        sql = f"""UPDATE {current_user} 
        SET UserNameOrEmail='{UserNameOrEmail}', 
        Password='{Password}', 
        Link='{Link}', 
        Notes='{Notes}'
        WHERE ID={ID}"""
        curs.execute(sql)
        conn.commit()
    except ValueError as e:
        tk.messagebox.showerror("show error", e)
    close()