import tkinter as tk
from tkinter import W, E, N, S, messagebox
from PIL import Image, ImageTk
from dbquery import *
def clean_entry_create():
    UserName_Entry.delete(0, tk.END)
    Phone_Entry.delete(0, tk.END)
    Email_Entry.delete(0, tk.END)
    Password_Entry.delete(0, tk.END)
    Password_retype_Entry.delete(0, tk.END)
def check_email(email):
    Answer = False
    for x in range(len(email)):
        if email[x] == '@':
            Answer = True
            break
    return Answer
def get_entry_create():
    SurName_Entry_var = UserName_Entry.get().strip()
    Phone_Entry_var = Phone_Entry.get().strip()
    Email_Entry_var = Email_Entry.get().strip()
    Password_Entry_var = Password_Entry.get().strip()
    Password_retype_Entry_var = Password_retype_Entry.get().strip()
    if Password_Entry_var != Password_retype_Entry_var:
        tk.messagebox.showerror("showerror", "The passwords are not same")
    else:
        if check_email(Email_Entry_var) == False:
            tk.messagebox.showerror("showerror", "wrong email")
        else:
            Answer = insert_data(SurName_Entry_var, Phone_Entry_var, Email_Entry_var, Password_Entry_var)
            if Answer == True:
                clean_entry_create()
                show_frame(frame_start)
                tk.messagebox.showinfo("Conformation", "Account has been created")
def show_frame(frame):
    frame.tkraise()
def get_entry_logIn():
    UserName_LogIn_Entry_var = UserName_LogIn_Entry.get().strip()
    Password_LogIn_Entry_var = Password_LogIn_Entry.get().strip()
    UserName_LogIn_Entry.delete(0, tk.END)
    Password_LogIn_Entry.delete(0, tk.END)
    return UserName_LogIn_Entry_var, Password_LogIn_Entry_var
def log_in():
    UserName_LogIn_Entry_var, Password_LogIn_Entry_var = get_entry_logIn()
    if Password_LogIn_Entry_var == select_password(UserName_LogIn_Entry_var):
        show_frame(frame_data)
    else:
        tk.messagebox.showerror('Error', 'Wrong username or password')
def double_click(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = listbox.get(selected_index[0])
        label.config(text=f'Selected: {selected_index}')
def WindowsTK():
    global UserName_Entry, Phone_Entry, Email_Entry, Password_Entry, Password_retype_Entry, frame_start, frame_data
    global UserName_LogIn_Entry, Password_LogIn_Entry
    global listbox, label
    window = tk.Tk()
    window.geometry('800x600')
    window.resizable(False, False)
    window.title('PassSaver')
    original_image = Image.open(r"C:\Users\zange\source\repos\Zhan-Gabriel-Gerke\project-test\FinalWork\background.jpg")
    resized_image = original_image.resize((800, 600))
    bgimage = ImageTk.PhotoImage(resized_image)
    container = tk.Frame(window)
    container.pack(fill="both", expand=True)
    frame_create = tk.Frame(container)
    frame_log_in = tk.Frame(container)
    frame_start = tk.Frame(container)
    frame_data = tk.Frame(container)
    for frame in (frame_create, frame_log_in, frame_start, frame_data):
        frame.place(relwidth=1, relheight=1)
    labelBG= tk.Label(frame_start,image=bgimage)
    labelBG.place(x=0,y=0)
    labelBG= tk.Label(frame_log_in,image=bgimage)
    labelBG.place(x=0,y=0)
    labelBG= tk.Label(frame_create,image=bgimage)
    labelBG.place(x=0,y=0)
    labelBG= tk.Label(frame_data,image=bgimage)
    labelBG.place(x=0,y=0)
    welcome_lable = tk.Label(frame_start, bg='gray', text='PassKeeper', font=('Arial', 30, 'bold'))
    welcome_lable.place(x=300, y=80)
    Button_create = tk.Button(frame_start, text='Create new account', font=('Arial', 15, 'bold'), bg='gray', command=lambda: show_frame(frame_create))
    Button_create.place(x=320, y=200)
    Button_log_in = tk.Button(frame_start, text='Log In', font=('Arial', 15, 'bold'), bg='gray', command=lambda: show_frame(frame_log_in))
    Button_log_in.place(x=380, y=250)
    log_in_lable = tk.Label(frame_log_in, bg='gray', text='Log In', font=('Arial', 30, 'bold'))
    log_in_lable.place(x=350, y=50)
    create_new_accoun_lable = tk.Label(frame_create, bg='gray', text='Create new account', font=('Arial', 30, 'bold'))
    create_new_accoun_lable.place(x=250, y=50)
    Button_back_login = tk.Button(frame_log_in, text='Back', font=('Arial', 15, 'bold'), bg='gray', command=lambda: show_frame(frame_start))
    Button_back_login.place(x=700, y=550)
    Button_back_login = tk.Button(frame_create, text='Back', font=('Arial', 15, 'bold'), bg='gray', command=lambda: show_frame(frame_start))
    Button_back_login.place(x=700, y=550)
    Username_Lable = tk.Label(frame_create, text='Username', font=('Arial', 15, 'bold'), bg='gray')
    Username_Lable.place(x=100, y=230)
    Phone_Lable = tk.Label(frame_create, text='Phone', font=('Arial', 15, 'bold'), bg='gray')
    Phone_Lable.place(x=100, y=260)
    Email_Lable = tk.Label(frame_create, text='e-mail', font=('Arial', 15, 'bold'), bg='gray')
    Email_Lable.place(x=100, y=290)
    Password_Lable = tk.Label(frame_create, text='Password', font=('Arial', 15, 'bold'), bg='gray')
    Password_Lable.place(x=100, y=320)
    Password_retype_Lable = tk.Label(frame_create, text='Re-Type', font=('Arial', 15, 'bold'), bg='gray')
    Password_retype_Lable.place(x=100, y=350)
    UserName_Entry = tk.Entry(frame_create, bg='lightgray', font=('Arial',15,'bold'))
    UserName_Entry.place(x=200, y=230)
    Phone_Entry = tk.Entry(frame_create, bg='lightgray', font=('Arial',15,'bold'))
    Phone_Entry.place(x=200, y=260)
    Email_Entry = tk.Entry(frame_create, bg='lightgray', font=('Arial',15,'bold'))
    Email_Entry.place(x=200, y=290)
    Password_Entry = tk.Entry(frame_create, bg='lightgray', font=('Arial',15,'bold'))
    Password_Entry.place(x=200, y=320)
    Password_retype_Entry = tk.Entry(frame_create, bg='lightgray', font=('Arial',15,'bold'))
    Password_retype_Entry.place(x=200, y=350)
    Password_requirements_Label = tk.Label(frame_create, bg='gray', font=('Arial', 15, 'bold'), text="""The Password must have more that 10 characters. 
    contain more that one Uppercase and Lowercase letters. 
    And it have include more than one specific symbol""")
    Password_requirements_Label.place(x=100, y=400)
    Create_button = tk.Button(frame_create, bg='lightgray', text='Create', font=('Arial', 15, 'bold'), command=get_entry_create)
    Create_button.place(x=300, y=500)
    UserName_LogIn_Label = tk.Label(frame_log_in, bg='gray', text='UserName', font=('Arial', 15, 'bold'))
    UserName_LogIn_Label.place(x=100, y=200)
    UserName_LogIn_Entry = tk.Entry(frame_log_in, bg='lightgray', font=('Arial',15, 'bold'))
    UserName_LogIn_Entry.place(x=220, y=200)
    Password_LogIn_Label = tk.Label(frame_log_in, bg='gray', font=('Arial',15, 'bold'), text='Password')
    Password_LogIn_Label.place(x=100, y=230)
    Password_LogIn_Entry = tk.Entry(frame_log_in, bg='lightgray', font=('Arial',15, 'bold'))
    Password_LogIn_Entry.place(x=220, y=230)
    LogIn_Button = tk.Button(frame_log_in, bg='gray', font=('Arial', 15, 'bold'), text='Log In', command=log_in)
    LogIn_Button.place(x=300, y=300)
    listbox = tk.Listbox(frame_data)
    listbox.place(x=0, y=0)
    items = ['One', 'Two', 'Three', 'Four']
    for item in items:
        listbox.insert(tk.END, item)
    listbox.bind("<Double-Button-1>", double_click)
    label = tk.Label(frame_data, text='Selected: ')
    label.place(x=200, y=200)
    show_frame(frame_start)
    window.mainloop()