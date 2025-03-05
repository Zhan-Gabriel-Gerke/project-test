import tkinter as tk
from tkinter import W, E, N, S, Entry, messagebox
def tkwindow():
    global Label1
    global Label2
    global Entry1
    global Entry2
    global Entry3
    global Button1
    global Button2
    global Button3
    window = tk.Tk()
    window.geometry('500x600')
    window.resizable(False, False)
    window.title('Numerology')
    Label1 = tk.Label(window, bg='lightgreen', font=('Arial',20,'bold'), text='Enter you BirthDate', width = 20)
    Label1.place(x=80, y=15)
    Entry1 = tk.Entry(window, bg="lightblue", font=('Arial',20,'bold'), width = 23)
    Entry1.place(x=80, y=50)
    Button1 = tk.Button(window, text='Start', font=('Arial', 20, 'bold'))
    Button1.place(x=200, y=90)
    Label2 = tk.Label(window, font=('Arial', 20, 'bold'), bg='red', width = 20, text="Here you'll see an answer")
    Label2.place(x=80, y=150)
    Button2 = tk.Button(window, text='Save result', font=('Arial', 20, 'bold'))
    Button2.place(x=165, y=190)
    Button3 = tk.Button(window, text='Show previous results', font=('Arial', 20, 'bold'))
    Button3.place(x=90, y=250)
    window.mainloop()
def whichaplhabet(Name):
    ENG = ['z','x','c','v','b','n','m','a','s',
           'd','f','g','h','j','k','l','q','w',
           'e','r','t','y','u','i','o','p']
    RUS = ['я','ч','с','м','и','т','ь','б','ю',
           'ф','ы','в','а','п','р','о','л','д',
           'ж','э','й','ц','у','к','е','н','г',
           'ш','щ','з','х','ъ']