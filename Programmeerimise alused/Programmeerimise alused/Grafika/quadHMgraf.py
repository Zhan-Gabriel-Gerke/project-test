import tkinter as tk
import math
def quadurav(a, b, c):
    a, b, c = int(a), int(b), int(c)
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = ((-1 * b) + math.sqrt(D)) / (2 * a)
        x2 = ((-1 * b) - math.sqrt(D)) / (2 * a)
        print(D)
        roots = f'D = {D}, X1 = {x1}, X2 = {x2}'
    elif D == 0:
        x = (-1 * b) / (2 * a)
        roots = f'D = {D} ,X = {x}'
    elif D < 0:
        roots = 'D < 0'
    label_5.configure(text = roots, font='Arial 20')   
def get_data_entry():
    agde = entry_1.get()
    bgde = entry_2.get()
    cgde = entry_4.get()
    delite_entry()
    quadurav(agde, bgde, cgde)
def delite_entry():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_4.delete(0, tk.END)
window = tk.Tk()
window.geometry('600x170')
window.resizable(False, False)
window.title('Square levels')
label_1 = tk.Label(window, text='Solving a quadratic level',
                bg='lightblue',
                fg='green',
                font=('Arial',20,'bold'))
entry_1 = tk.Entry(window,
                   bg='lightblue',
                   fg='green',
                   width=4,
                   font=('Arial',20,'bold')
                   )
label_2 = tk.Label(window, text='x**2+',
                   fg='green',
                   font=('Arial',20,'bold'))
entry_2 = tk.Entry(window,
                   bg='lightblue',
                   fg='green',
                   font=('Arial',20,'bold'),
                   width=4
                   )
label_3 = tk.Label(window, text='x+',
                   fg='green',
                   font=('Arial',20,'bold'))
entry_4 = tk.Entry(window,
                   bg='lightblue',
                   fg='green',
                   font=('Arial',20,'bold'),
                   width=4
                   )
label_4 = tk.Label(window, text='=0',
                   fg='green',
                   font=('Arial',20,'bold'))
button_1 = tk.Button(window, text='Solve',
                     bg='green',
                     font=('Arial',20,'bold'),
                     command=get_data_entry)
label_6 = tk.Label(window, text='  ')
label_7 = tk.Label(window, text='  ')
label_5 = tk.Label(window, text='Answer',
                   bg='yellow',
                   font=('Arial',20,'bold'),
                   width=20)
label_1.grid(row=0, column=1, columnspan=5)
entry_1.grid(row=1, column=0)
label_2.grid(row=1, column=1)
entry_2.grid(row=1, column=2)
label_3.grid(row=1, column=3)
entry_4.grid(row=1, column=4)
label_4.grid(row=1, column=5)
button_1.grid(row=1, column=6)
label_6.grid(row=2, column=0, columnspan=6, ipady=5)
label_7.grid(row=3, column=0, columnspan=6, ipady=5)
label_5.grid(row=3, column=3, columnspan=5, ipady=5)
window.mainloop()
