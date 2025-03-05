import tkinter as tk
from tkinter import W, E, N, S, messagebox, filedialog
from email.message import EmailMessage
import smtplib, ssl, imghdr, os
from click import command, password_option
def image_add():
    global file
    file=filedialog.askopenfilename()
    label_lisa3.configure(text=file)
def email():
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'testmailfortthk@gmail.com'
    #####https://myaccount.google.com/apppasswords
    password = 'esmd plst aeln ydln'
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(entry_kiri_var)
    msg['Subject'] = entry_teema_var
    msg['From'] = sender_email
    msg['To'] = entry_email_var
    if "file" in globals():
        with open(file, 'rb') as fpilt:
            pilt=fpilt.read()
        msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        messagebox.showinfo('Kiri oli saadetud')
        print('Sent')
    except Exception as e:
        print('Error:', e)
def start():
    get_data_entry()
    delite_entry()
    email()
def write_to_file():
    with open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Grafika\on_exit.txt', "w", encoding="utf-8") as f:
        TempVariable = f'{entry_email.get()}◆{entry_teema.get()}◇{entry_kiri.get("1.0", tk.END)}'
        f.write(TempVariable)
def read_from_file():
    global entry_email_var, entry_teema_var, entry_kiri_var
    file = r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Grafika\on_exit.txt'
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()
        n1 = data.find('◆')
        n2 = data.find('◇')
        entry_email_var, entry_teema_var, entry_kiri_var = data[0:n1].strip(), data[n1+1:n2].strip(), data[n2+1:len(data)].strip()
        return entry_email_var, entry_teema_var, entry_kiri_var
def before_start():
    global entry_email_var, entry_teema_var, entry_kiri_var
    file_path = r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Grafika\on_exit.txt'
    if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
        TrueOrFalse = messagebox.askyesno("A draft has been found", "Would you like to use a draft?")
        if TrueOrFalse == True:
            read_from_file()
            print(entry_email_var, entry_teema_var, entry_kiri_var)
            entry_email.insert(0, entry_email_var)
            entry_kiri.insert(1.0, entry_kiri_var)
            entry_teema.insert(0, entry_teema_var)
        # print(entry_email_var, entry_teema_var, entry_kiri_var, 'before_start')
    # else:
    #     global entry_email_var, entry_teema_var, entry_kiri_var
def on_exit():
    # entry_email_var, entry_teema_var, entry_kiri_var = None
    write_to_file()
    window.destroy()
def get_data_entry():
    # global entry_email_var, entry_teema_var, entry_kiri_var
    entry_email_var = entry_email.get()
    entry_teema_var = entry_teema.get()
    entry_kiri_var = entry_kiri.get(1.0, tk.END)
def delite_entry():
    entry_email.delete(0, tk.END)
    entry_teema.delete(0, tk.END)
    entry_kiri.delete("1.0", tk.END)
    if "file" in globals():
        label_lisa3.configure(text='...')
#global entry_email_var, entry_teema_var, entry_kiri_var
def test():
    window = tk.Tk()
    window.geometry('500x600')
    window.resizable(False, False)
    window.title('E-mail sender')
    window.protocol("WM_DELETE_WINDOW", on_exit)
    label_email = tk.Label(window, text='EMAIL: ', font=('Arial',20,'bold'), bg='green', fg='white')
    label_teema = tk.Label(window, text='TEEMA: ', font=('Arial',20,'bold'), bg='green', fg='white')
    label_lisa = tk.Label(window, text='LISA: ', font=('Arial',20,'bold'), bg='green', fg='white')
    entry_email = tk.Entry(window, bg='lightgreen', font=('Arial',15,'bold'))
    entry_teema = tk.Entry(window, bg='lightgreen', font=('Arial',15,'bold'))
    label_lisa3 = tk.Label(window, text='...', font=('Arial',10,'bold'), bg='lightgreen', fg='white')
    entry_kiri = tk.Text(window, bg='lightgreen', font='Arial 10', width=40)
    label_kiri = tk.Label(window, text='Kiri', font=('Arial',20,'bold'), bg='green', fg='white')
    button_lisa = tk.Button(window, text='LISA PILT', font=('Arial', 15, 'bold'), command=image_add)
    button_saada = tk.Button(window, text='SAADA', font=('Arial', 15, 'bold'), command=start)
    label_email.grid(row=0, column=0, sticky=W+E+N+S)
    label_teema.grid(row=1, column=0, sticky=W+E+N+S)
    label_lisa.grid(row=2, column=0, sticky=W+E+N+S)
    entry_email.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
    entry_teema.grid(row=1, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
    label_lisa3.grid(row=2, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
    label_kiri.grid(row=4, column=0, padx = 20, sticky=W)
    entry_kiri.grid(row=3, column=1, columnspan=5, rowspan=2, sticky=W+E+N+S, padx = 20)
    button_lisa.grid(row=8, column=1, padx = 20)
    button_saada.grid(row=8, column=2)
    before_start()
    window.mainloop()