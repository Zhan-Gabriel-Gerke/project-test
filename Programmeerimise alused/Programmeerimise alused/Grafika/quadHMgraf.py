import tkinter as tk
window = tk.Tk()
window.geometry('600x200')
window.resizable(False, False)
window.title('Square levels')
label_1 = tk.Label(window, text='Solving a quadratic level',
                bg='lightblue',
                fg='green',
                font=('Arial',20,'bold'))
entry_1 = tk.Entry(window,
                   bg='lightblue',
                   )
label_1.grid(row=0, column=2)
entry_1.grid(row=1, column=0, ipady=10)
window.mainloop()