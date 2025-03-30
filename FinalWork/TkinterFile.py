import tkinter as tk
from tkinter import W, E, N, S, messagebox
from PIL import Image, ImageTk
from dbquery import *
import random
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
            ListOfSymbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-']
            UpCase, LwCase, SpSymbol = None, None, None
            if len(Password_Entry_var) >= 10:
                for x in range(len(Password_Entry_var)):
                    if Password_Entry_var[x].isupper():
                        UpCase = True
                    if Password_Entry_var[x].islower():
                        LwCase = True
                    if Password_Entry_var[x] in ListOfSymbols:
                        SpSymbol = True
            if LwCase == True and UpCase == True and SpSymbol == True:
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
def group_data(data):
    global link_list, UserName_list, id_list, listbox_list
    link_list, UserName_list, id_list, listbox_list = [], [], [], []
    for x in range(len(data)):
        list_list = data[x]
        ID = list_list[0]
        id_list.append(ID)
        UserName = list_list[1]
        UserName_list.append(UserName)
        Link = list_list[3]
        link_list.append(link_list)
        listbox = f'{UserName}; {Link}'
        listbox_list.append(listbox)
def log_in():
    global current_user
    UserName_LogIn_Entry_var, Password_LogIn_Entry_var = get_entry_logIn()
    if Password_LogIn_Entry_var == select_password(UserName_LogIn_Entry_var):
        show_frame(frame_data)
        current_user = UserName_LogIn_Entry_var
        data = select_data(current_user)
        group_data(data)
        listbox_def()
    else:
        tk.messagebox.showerror('Error', 'Wrong username or password')
def change_data_activator():
    ID = current_data[0]
    Username = UserName_edit_Entry.get()
    Password = Password_edit_Entry.get()
    Notes = Notes_edit_Entry.get()
    Link = Link_edit_Entry.get()
    #change_data(current_user, current_data[1], current_data[2], current_data[3], current_data[4], current_data[0])
    change_data(current_user, Username, Password, Link, Notes, ID)
    tk.messagebox.showinfo('Info', 'Data has been updated')
    back_to_frame_data()
def edit_active():
    global UserName_edit_Entry, Password_edit_Entry, Notes_edit_Entry, Link_edit_Entry
    try:
        if current_data:
            show_frame(frame_edit_data)
            Username_Lable = tk.Label(frame_edit_data, text='Username', font=('Arial', 15, 'bold'), bg='gray')
            Username_Lable.place(x=100, y=230)
            Link_Lable = tk.Label(frame_edit_data, text='Link', font=('Arial', 15, 'bold'), bg='gray')
            Link_Lable.place(x=100, y=260)
            Password_Lable = tk.Label(frame_edit_data, text='Password', font=('Arial', 15, 'bold'), bg='gray')
            Password_Lable.place(x=100, y=290)
            Notes_Lable = tk.Label(frame_edit_data, text='Notes', font=('Arial', 15, 'bold'), bg='gray')
            Notes_Lable.place(x=100, y=320)
            UserName_edit_Entry = tk.Entry(frame_edit_data, bg='lightgray', font=('Arial',15,'bold'))
            UserName_edit_Entry.place(x=200, y=230)
            Link_edit_Entry = tk.Entry(frame_edit_data, bg='lightgray', font=('Arial',15,'bold'))
            Link_edit_Entry.place(x=200, y=260)
            Password_edit_Entry = tk.Entry(frame_edit_data, bg='lightgray', font=('Arial',15,'bold'))
            Password_edit_Entry.place(x=200, y=290)
            Notes_edit_Entry = tk.Entry(frame_edit_data, bg='lightgray', font=('Arial',15,'bold'))
            Notes_edit_Entry.place(x=200, y=320)
            UserName_edit_Entry.insert(0, current_data[1])
            Link_edit_Entry.insert(0, current_data[3])
            Password_edit_Entry.insert(0,current_data[2])
            Notes_edit_Entry.insert(0,current_data[4])
            Save_Button = tk.Button(frame_edit_data, bg='gray', font=('Arial', 15, 'bold'), text='Save', command=change_data_activator)
            Save_Button.place(x=100, y=350)
            Back_Button = tk.Button(frame_edit_data, bg='gray', font=('Arial', 15, 'bold'), text='Back', command=back_to_frame_data)
            Back_Button.place(x=200, y=350)
    except:
        tk.messagebox.showerror('Error', "You haven't chosen a record")
    #change_data(current_user, UserNameOrEmail, Password, Link, Notes, ID)
def creare_frame_data(data):
    global Edit_data_Button, current_data
    data = data[0]
    UserName_Data_Lable_DATA.config(text=data[1])
    PSWD_Data_Lable_DATA.config(text=data[2])
    Link_Lable_DATA.config(text=data[3])
    Notes_Lable_DATA.config(text=data[4])
    current_data = data
def double_click(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = listbox.get(selected_index[0])
        # label.config(text=f'Selected: {selected_index}')
        temp_var = selected_index.split(';')
        for x in range(len(UserName_list)):
            if temp_var[0] == UserName_list[x]:
                User_ID = x + 1
                data = select_data_by_id(current_user, User_ID)
                creare_frame_data(data)
        # else:
        #     tk.messagebox.showerror('Error','Error def double_click')
def listbox_def():
    global label, listbox
    listbox = tk.Listbox(frame_data, width=55, height=37)
    listbox.place(x=0, y=0)
    for item in listbox_list:
        listbox.insert(tk.END, item)
    listbox.bind("<Double-Button-1>", double_click)
    # label = tk.Label(frame_data, text='Selected: ')
    # label.place(x=200, y=200)
def back_to_frame_data():
    data = select_data(current_user)
    group_data(data)
    listbox_def()
    show_frame(frame_data)
    UserName_Data_Lable_DATA.config(text='...')
    PSWD_Data_Lable_DATA.config(text='...')
    Link_Lable_DATA.config(text='...')
    Notes_Lable_DATA.config(text='...')
def log_out():
    show_frame(frame_start)
    UserName_Data_Lable_DATA.config(text='...')
    PSWD_Data_Lable_DATA.config(text='...')
    Link_Lable_DATA.config(text='...')
    Notes_Lable_DATA.config(text='...')
    #Edit_data_Button.destroy()
def create_account_crate_frame():
    UserName_var = UserName_Create_Entry.get()
    PSWD_var = PSWD_Create_Entry.get()
    Link_var = Link_Create_Entry.get()
    Notes_var = Notes_Create_Entry.get()
    if len(UserName_var) < 1 or len(PSWD_var) < 1:
        tk.messagebox.showerror('Error', "Wrong UserName or Password")
    else:
        YorN = add_data_to_table(current_user, UserName_var, PSWD_var, Link_var, Notes_var)
        if YorN == True:
            tk.messagebox.showinfo('Info', 'Account has been created')
        else:
            tk.messagebox.showerror('Error', "Account hasn't been created")
def randomPassword():
    Alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    Numbers = ['1','2','3','4','5','6','7','8','9','0']
    Symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-']
    password = '.'
    for x in range(12):
        from1to3 = random.randint(1,3)
        if from1to3 == 1:
            random_var = random.randint(1, len(Alphabet)-1)
            var = Alphabet[random_var]
            print(random_var)
            if random_var % 2 == 0:
                var = var.upper()
                print('fiewfoiwejfioewjkflew')
            password = password + var
        elif from1to3 ==2:
            random_var = random.randint(1, len(Numbers)-1)
            var = Numbers[random_var]
            password = password + str(var)
        elif from1to3 ==3:
            random_var = random.randint(1, len(Symbols)-1)
            var = Symbols[random_var]
            password = password + var
    password = password[1:]
    Password_Entry.insert(0, password)
    Password_retype_Entry.insert(0, password)
def back_from_create():
    show_frame(frame_start)
    Password_Entry.delete(0, tk.END)
    Password_retype_Entry.delete(0, tk.END)
def WindowsTK():
    global UserName_Entry, Phone_Entry, Email_Entry, Password_Entry, Password_retype_Entry, frame_start, frame_data, frame_edit_data
    global UserName_LogIn_Entry, Password_LogIn_Entry
    global listbox, label, UserName_Data_Lable_DATA, PSWD_Data_Lable_DATA, Link_Lable_DATA, Notes_Lable_DATA
    global UserName_Create_Entry, PSWD_Create_Entry, Link_Create_Entry, Notes_Create_Entry, Edit_data_Button
    global Password_Entry, Password_retype_Entry
    #create root window
    window = tk.Tk()
    window.geometry('800x600')
    window.resizable(False, False)
    window.title('PassSaver')
    #background
    original_image = Image.open(r"C:\Users\zange\source\repos\Zhan-Gabriel-Gerke\project-test\FinalWork\background.jpg")
    resized_image = original_image.resize((800, 600))
    bgimage = ImageTk.PhotoImage(resized_image)
    #create Frames
    container = tk.Frame(window)
    container.pack(fill="both", expand=True)
    frame_create = tk.Frame(container)
    frame_log_in = tk.Frame(container)
    frame_start = tk.Frame(container)
    frame_data = tk.Frame(container)
    frame_add_account = tk.Frame(container)
    frame_edit_data = tk.Frame(container)
    for frame in (frame_create, frame_log_in, frame_start, frame_data, frame_add_account, frame_edit_data):
        frame.place(relwidth=1, relheight=1)
    #background
    labelBG= tk.Label(frame_start,image=bgimage)
    labelBG.place(x=0,y=0)
    labelBG= tk.Label(frame_log_in,image=bgimage)
    labelBG.place(x=0,y=0)
    labelBG= tk.Label(frame_create,image=bgimage)
    labelBG.place(x=0,y=0)
    labelBG= tk.Label(frame_data,image=bgimage)
    labelBG.place(x=0,y=0)
    labelBG= tk.Label(frame_add_account,image=bgimage)
    labelBG.place(x=0,y=0)
    labelBG= tk.Label(frame_edit_data,image=bgimage)
    labelBG.place(x=0,y=0)
    #frame_start
    welcome_lable = tk.Label(frame_start, bg='gray', text='PassKeeper', font=('Arial', 30, 'bold'))
    welcome_lable.place(x=300, y=80)
    Button_create = tk.Button(frame_start, text='Create new account', font=('Arial', 15, 'bold'), bg='gray', command=lambda: show_frame(frame_create))
    Button_create.place(x=320, y=200)
    Button_log_in = tk.Button(frame_start, text='Log In', font=('Arial', 15, 'bold'), bg='gray', command=lambda: show_frame(frame_log_in))
    Button_log_in.place(x=380, y=250)
    #frame_log_in
    log_in_lable = tk.Label(frame_log_in, bg='gray', text='Log In', font=('Arial', 30, 'bold'))
    log_in_lable.place(x=350, y=50)
    create_new_accoun_lable = tk.Label(frame_create, bg='gray', text='Create new account', font=('Arial', 30, 'bold'))
    create_new_accoun_lable.place(x=250, y=50)
    Button_back_login = tk.Button(frame_log_in, text='Back', font=('Arial', 15, 'bold'), bg='gray', command=lambda: show_frame(frame_start))
    Button_back_login.place(x=700, y=550)
    #frame_create
    Button_back_login = tk.Button(frame_create, text='Back', font=('Arial', 15, 'bold'), bg='gray', command=back_from_create)
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
    And it have include more than one specific symbol
              Symbols : (!@#$%^&*()_+=-)""")
    Password_requirements_Label.place(x=100, y=400)
    Create_button = tk.Button(frame_create, bg='lightgray', text='Create', font=('Arial', 15, 'bold'), command=get_entry_create)
    Create_button.place(x=200, y=500)
    Random_Password_Button = tk.Button(frame_create, bg='lightgray', text='Random Password', font=('Arial', 15, 'bold'), command=randomPassword)
    Random_Password_Button.place(x=350, y=500)
    #frame_log_in
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
    #frame_data
    UserName_Baner_Data_Lable = tk.Label(frame_data, bg='gray', font=('Arial', 15, 'bold'), text='Username:')
    UserName_Baner_Data_Lable.place(x=350, y=200)
    UserName_Data_Lable = tk.Label(frame_data, bg='gray', font=('Arial', 15, 'bold'), text='Password:')
    UserName_Data_Lable.place(x=350, y=250)
    Link_Lable = tk.Label(frame_data, bg='gray', font=('Arial', 15, 'bold'), text='Link:')
    Link_Lable.place(x=350, y=300)
    Notes_Lable = tk.Label(frame_data, bg='gray', font=('Arial', 15, 'bold'), text='Notes:')
    Notes_Lable.place(x=350, y=350)
    UserName_Data_Lable_DATA = tk.Label(frame_data, bg='lightgray', font=('Arial', 15, 'bold'), text='...', width=20)
    UserName_Data_Lable_DATA.place(x=500, y=200)
    PSWD_Data_Lable_DATA = tk.Label(frame_data, bg='lightgray', font=('Arial', 15, 'bold'), text='...', width=20)
    PSWD_Data_Lable_DATA.place(x=500, y=250)
    Link_Lable_DATA = tk.Label(frame_data, bg='lightgray', font=('Arial', 15, 'bold'), text='...', width=20)
    Link_Lable_DATA.place(x=500, y=300)
    Notes_Lable_DATA = tk.Label(frame_data, bg='lightgray', font=('Arial', 15, 'bold'), text='...', width=20)
    Notes_Lable_DATA.place(x=500, y=350)
    LogOut_Button = tk.Button(frame_data, bg='gray', font=('Arial', 15, 'bold'), text='Log Out', command=log_out)
    LogOut_Button.place(x=680, y=530)
    Add_Account = tk.Button(frame_data, bg='gray', font=('Arial', 15, 'bold'), text='Add Account', command=lambda: show_frame(frame_add_account))
    Add_Account.place(x=400, y=530)
    Edit_data_Button = tk.Button(frame_data,text='Edit', font=('Arial', 15, 'bold'), bg='gray', command=edit_active)
    Edit_data_Button.place(x=350, y=400)
    #Frame Add Account
    Banner_Create_Label = tk.Label(frame_add_account, bg='gray', font=('Arial', 15, 'bold'), text='Enter data')
    Banner_Create_Label.place(x=350, y=50)
    UserName_Baner_Create_Lable = tk.Label(frame_add_account, bg='gray', font=('Arial', 15, 'bold'), text='Username:')
    UserName_Baner_Create_Lable.place(x=150, y=200)
    UserName_Create_Lable = tk.Label(frame_add_account, bg='gray', font=('Arial', 15, 'bold'), text='Password:')
    UserName_Create_Lable.place(x=150, y=250)
    Link_Create_Lable = tk.Label(frame_add_account, bg='gray', font=('Arial', 15, 'bold'), text='Link:')
    Link_Create_Lable.place(x=150, y=300)
    Notes_Create_Lable = tk.Label(frame_add_account, bg='gray', font=('Arial', 15, 'bold'), text='Notes:')
    Notes_Create_Lable.place(x=150, y=350)
    UserName_Create_Entry = tk.Entry(frame_add_account, bg='lightgray', font=('Arial', 15, 'bold'), width=20)
    UserName_Create_Entry.place(x=300, y=200)
    PSWD_Create_Entry = tk.Entry(frame_add_account, bg='lightgray', font=('Arial', 15, 'bold'), width=20)
    PSWD_Create_Entry.place(x=300, y=250)
    Link_Create_Entry = tk.Entry(frame_add_account, bg='lightgray', font=('Arial', 15, 'bold'), width=20)
    Link_Create_Entry.place(x=300, y=300)
    Notes_Create_Entry = tk.Entry(frame_add_account, bg='lightgray', font=('Arial', 15, 'bold'), width=20)
    Notes_Create_Entry.place(x=300, y=350)
    Create_Account_Create_Button = tk.Button(frame_add_account ,text='Create Account' ,bg='gray', font=('Arial', 15, 'bold'), command=create_account_crate_frame)
    Create_Account_Create_Button.place(x=320, y=420)
    Back_Create_Button = tk.Button(frame_add_account, text='Back', bg='gray', font=('Arial', 15, 'bold'), command=back_to_frame_data)
    Back_Create_Button.place(x=700, y=540)
    show_frame(frame_start)
    window.mainloop()