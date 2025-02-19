from tkinter import *
from file.py import *
def figuur():
    pass



aken=Tk() #model for window
aken.geometry('800x400')
aken.title("Graafikud")
pealkiri = Label(aken, text='Erinevad piltid Matplotlib abil', font="Calibri 24", fg='green', bg='yellow', padx=20)

var=IntVar()
r1 = Radiobutton(aken, text='Prillid', font = 'Calibri 18', variable=var, value=1, command=figuur)
r2 = Radiobutton(aken, text='Kitt', font = 'Calibri 18', variable=var, value=2, command=figuur)


pealkiri.pack()
aken.mainloop()