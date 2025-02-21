from tkinter import *
from file import *
global varv, tekst
def varvi_valik():
    global varv, tekst
    varv = 'white'
    if tekst.get()!='':
        tekst.configure(bg='yellow')
        varv=tekst.get()
    else:
        tekst.configure(bg='red')
    return varv
def figuur(varv:str):
    valik=var.get()
    varv=varvi_valik()
    if valik==1:
        otsti(varv)
    elif valik==2:
        kitt(varv)
 
aken=Tk() #model for window
aken.geometry('800x400')
aken.title("Graafikud")
pealkiri = Label(aken, text='Erinevad piltid Matplotlib abil', font="Calibri 24", fg='green', bg='yellow', padx=20)

var=IntVar()
r1 = Radiobutton(aken, text='Prillid', font = 'Calibri 18', variable=var, value=1, command=figuur)
r2 = Radiobutton(aken, text='Kitt', font = 'Calibri 18', variable=var, value=2, command=figuur)
tekst = Entry(aken, font='Calibri 24', fg='green', bg='yellow', width=200)
nupp=Button(aken, text='Varvi valik', font='Calibri 24', fg='green', bg='yellow', command=varvi_valik)






pealkiri.pack() #place(x= ..., y= ...) grid(c=...., row=.....)
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
aken.mainloop()
