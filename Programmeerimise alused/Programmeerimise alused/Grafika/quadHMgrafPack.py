from tkinter import *

def aken():
    aken=Tk()
    aken.geometry("650x260")
    aken.title("Ruutvorand")
    f1=Frame(aken, width=650, height=260)
    f1.pack
    lbl=Label(f1, text="Ruutvorrandite lahendamine", font="Calibri 26", fg="green", bg="lightblue")
    lbl.pack(side=TOP)
    lbl_vastus=Label(f1, text="Lahendamine", height=4, width=60, bg="yellow")
    lbl_vastus.pack(side=BOTTOM)
    lbl_a=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
    lbl_a.pack(side=LEFT)
    x2=Label(f1, text="x^2", font="Calibri 26", fg="green", padx=10)
    x2.pack(side=LEFT)
    aken.mainloop()
aken()

# Не работает