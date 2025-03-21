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
def create_custom_table(email):
    opendb()
    sql = f""" CREATE TABLE IF NOT EXISTS {email}(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserNameOrEmail VARCHAR(30),
    Password VARCHAR(30),
    Link TEXT,
    Notes TEXT);"""
    curs.execute(sql)
def insert_data(Name, SurName, Phone, Email, Password):
    opendb()
    try:
        sql = f"""INSERT INTO users (Name, SurName, Phone, Email, Password)
        VALUES('{Name}', '{SurName}', '{Phone}', '{Email}', '{Password}')"""
        curs.execute(sql)
        conn.commit()
        create_custom_table(Email)
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