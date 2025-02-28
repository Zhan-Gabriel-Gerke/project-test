import tkinter as tk
from tkinter import W, E, N, S, messagebox, filedialog
from email.message import EmailMessage
import smtplib, ssl
import imghdr

from click import command
def image_add():
    global file
    file=filedialog.askopenfilename()
    label_lisa3.configure(text=file)
def email(entry_email_var, subject, letter):
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'testmailfortthk@gmail.com'
    #####https://myaccount.google.com/apppasswords
    password = 'esmd plst aeln ydln'
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(letter)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = entry_email_var
    with open(file, 'rb') as fpilt:
        pilt=fpilt.read()
    msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo('Kiri oli saadetud')
        print('Sent')
    except Exception as e:
        print('Error:', e)
def get_data_entry():
    entry_email_var = entry_email.get()
    entry_teema_var = entry_teema.get()
    entry_kiri_var = entry_kiri.get(1.0, tk.END)
    delite_entry()
    email(entry_email_var, entry_teema_var, entry_kiri_var)
def delite_entry():
    entry_email.delete(0, tk.END)
    entry_teema.delete(0, tk.END)
    entry_kiri.delete("1.0", tk.END)
window = tk.Tk()
window.geometry('500x600')
window.resizable(False, False)
window.title('E-mail sender')
# label_1 = tk.Label(window, text='Solving a quadratic level',
#                 bg='lightblue',
#                 fg='green',
#                 font=('Arial',20,'bold'))
# entry_1 = tk.Entry(window,
#                    bg='lightblue',
#                    fg='green',
#                    width=4,
#                    font=('Arial',20,'bold')
#                    )
# button_1 = tk.Button(window, text='Solve',
#                      bg='green',
#                      font=('Arial',20,'bold'),
#                      command=get_data_entry)
# label_1.grid(row=0, column=0, columnspan=8)
label_email = tk.Label(window, text='EMAIL: ', font=('Arial',20,'bold'), bg='green', fg='white')
label_teema = tk.Label(window, text='TEEMA: ', font=('Arial',20,'bold'), bg='green', fg='white')
label_lisa = tk.Label(window, text='LISA: ', font=('Arial',20,'bold'), bg='green', fg='white')
entry_email = tk.Entry(window, bg='lightgreen', font=('Arial',15,'bold'))
entry_teema = tk.Entry(window, bg='lightgreen', font=('Arial',15,'bold'))
label_lisa3 = tk.Label(window, text='...', font=('Arial',10,'bold'), bg='lightgreen', fg='white')
entry_kiri = tk.Text(window, bg='lightgreen', font='Arial 10', width=40)
label_kiri = tk.Label(window, text='Kiri', font=('Arial',20,'bold'), bg='green', fg='white')
button_lisa = tk.Button(window, text='LISA PILT', font=('Arial', 15, 'bold'), command=image_add)
button_saada = tk.Button(window, text='SAADA', font=('Arial', 15, 'bold'), command=get_data_entry)
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
window.mainloop()