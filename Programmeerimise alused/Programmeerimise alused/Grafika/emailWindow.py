from ipaddress import collapse_addresses
import tkinter as tk
from tkinter import W, E, N, S


window = tk.Tk()
window.geometry('600x600')
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
label_lisa3 = tk.Label(window, text='...', font=('Arial',20,'bold'), bg='lightgreen', fg='white')
entry_kiri = tk.Text(window, bg='lightgreen', font='Arial 10')
label_kiri = tk.Label(window, text='Kiri', font=('Arial',20,'bold'), bg='green', fg='white')
button_lisa = tk.Button(window, text='LISA PILT', font=('Arial', 20, 'bold'))
button_saada = tk.Button(window, text='SAADA', font=('Arial', 20, 'bold'))
label_email.grid(row=0, column=0, sticky=W+E+N+S)
label_teema.grid(row=1, column=0, sticky=W+E+N+S)
label_lisa.grid(row=2, column=0, sticky=W+E+N+S)
entry_email.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
entry_teema.grid(row=1, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
label_lisa3.grid(row=2, column=1, columnspan=2, sticky=W+E+N+S, padx = 20)
label_kiri.grid(row=4, column=0, padx = 20, sticky=W+E+N+S)
entry_kiri.grid(row=3, column=1, columnspan=5, rowspan=2, sticky=W+E+N+S, padx = 20)
button_lisa.grid(row=8, column=1, padx = 20)
button_saada.grid(row=8, column=2)
window.mainloop()