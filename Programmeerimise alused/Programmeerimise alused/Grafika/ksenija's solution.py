from turtle import color
from matplotlib.typing import MarkerType
import numpy as np #x=[min, max]
import matplotlib.pyplot as pl
from tkinter import *
from tkinter import messagebox
from turtle import color
import matplotlib.pyplot as plt

from PIL import Image, ImageTk


global D, x1, x2, x, i, y

def Solve():
    try:
        a = float(entryA.get())
        b = float(entryB.get())
        c = float(entryC.get())

        D = b**2 - 4* a * c

        if D>0:
            x1=round((-b+(D**(1/2)))/(2*a),2)
            x2=round((-b-(D**(1/2)))/(2*a),2)
            label5.configure(text=f"D > 0 --> 2 решения: \n x1 = {x1}\n x2 = {x2}")
            Graph2x(x1,x2)

        elif D == 0:
            x =round((-b / (2*a)), 2)
            label5.configure(text=f"D = 0 --> 1 решение: \n x = {x}")
            Graph1X()


        else:
            label5.configure(text="Решений нет")
        
    except:
        messagebox.showerror("error", 
        """ 
             /\_/\  
            ( ╬ಠ益ಠ)  
            ( つ ϞϞ  
        """)

def entryColor(event):
    i=entryA.get()
    if i == "":
        entryA.configure(bg="red")
    else:
        entryA.configure(bg="#ffe6f0")

    i=entryB.get()
    if i == "":
        entryB.configure(bg="red")
    else:
        entryB.configure(bg="#ffe6f0")
    i=entryC.get()
    if i == "":
        entryC.configure(bg="red")
    else:
        entryC.configure(bg="#ffe6f0")
#  For me:
#In Tkinter, when you bind a function to an event (like a key press or mouse click), 
#Tkinter automatically passes an event object as an argument to the function.

# # ГРАФИК
def Graph1X():
    a = float(entryA.get())
    b = float(entryB.get())
    c = float(entryC.get())
    x=np.linspace(-20, 20, 100)
    y = a * x**2 + b * x + c 

    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()


def Graph2x(x1,x2):
    a = float(entryA.get())
    b = float(entryB.get())
    c = float(entryC.get())
    x=np.linspace(x1 - 2, x2 + 2, 100)
    y = a * x**2 + b * x + c 

    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()




root=Tk()
root.geometry("900x400")
root.resizable(False,False)
root.title("Решение квадратного уравнения")


# bgimage=PhotoImage(file=r"C:\Users\SeagullToon\source\repos\kseniaTARgv24\targv24.Ksenia.1\graphic interface\text.png")
original_image = Image.open(r"C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Grafika\desktop.jpg")
resized_image = original_image.resize((900, 400))  # Resize to window size
bgimage = ImageTk.PhotoImage(resized_image)


labelBG=Label(root,image=bgimage)
labelBG.place(x=0,y=0)

label1 = Label(root, text = "Решение квадратного уравнения", font=("beer money", 20), bg= "#ffccff")
label1.pack(pady="20")

entryA= Entry(root, font=("beer money", 40), bg="#ffe6f0")
entryA.place(x=40,y=180, width=100)
entryA.bind("<KeyRelease>" ,entryColor)

label2=Label(root, font=("beer money", 40), text="x^2 +", bg="white")
label2.place(x=150, y=180)

entryB= Entry(root, font=("beer money", 40), bg="#ffe6f0")
entryB.place(x=275,y=180, width=100)
entryB.bind("<KeyRelease>" ,entryColor)

label3=Label(root, font=("beer money", 40), text="x +", bg="white")
label3.place(x=385, y=180)

entryC= Entry(root, font=("beer money", 40), bg="#ffe6f0")
entryC.place(x=465,y=180, width=100)
entryC.bind("<KeyRelease>" ,entryColor)

label4=Label(root, font=("beer money", 40), text="=0", bg="white")
label4.place(x=575, y=180)



button1=Button(root,text="Решить",font=("beer money", 45), command= Solve, bg="#ffe6e6")
button1.place(x=650, y = 140)


label5=Label(root, text="Ответ...",bg = "#ddccff", compound="center",)
label5.place(x=120, y= 290, width=600, height=90)






root.mainloop()
def Vaal(Color:str):
    x1=np.arange(0,10, 1) # 0, 1,2,3,4,5,6,7,8,9
    y1=(2/27)*x1**2-3

    x2=np.arange(-10, 1, 1)
    y2=0.04*x2**2-3

    x3=np.arange(-9, -2, 1)
    y3=(2/9)*(x3+6)**2+1

    x4=np.arange(-3, 10, 1)
    y4=(-1/12)*(x4-3)**2+6

    x5=np.arange(5, 9, 1)
    y5=(1/9)*(x5-5)**2+2

    x6=np.arange(5, 9, 1)
    y6=(1/8)*(x6-7)**2+1.5

    x7=np.arange(-13, -8, 1)
    y7=(-0.75)*(x7+11)**2+6

    x8=np.arange(-15, -11, 1)
    y8=(-0.5)*(x8+13)**2+3

    x9=np.arange(-15, -10, 1)
    y9=[1]*len(x9)

    x10 = np.arange(3, 5, 1)
    y10 = [3]*len(x10)

    pl.figure(facecolor = "green")
    pl.title("Vaal")
    pl.xlabel("X")
    pl.ylabel("Y")
    pl.grid(True)
    ax=pl.axes()
    ax.set_facecolor("blue")

    colors=["c" , "m" , "y" , "r" , "g" , "b", "w", "k","k","k"]

    # pl.plot(x1, y1,'r*-' )

    for i in range (1, 11, 1):
        pl.plot(eval(f"x{i}"), eval(f"y{i}"), Color[0]+'-')

    pl.show()


def Vihmavari(Color:str):

    x1=np.linspace(-12, 13,100 ) # 3th --- amount of points
    y1=(-1/18)*x1**2+12

    x2=np.arange(-4,5,1)
    y2=(-1/8)*x2**2+6

    x3=np.arange(-12,-3,1)
    y3=(-1/8)*(x3+8)**2+6

    x4 = np.arange(4, 13,1)
    y4=(-1/8)*(x4-8)**2+6

    x5=np.arange(-4, 1, 1 )
    y5=2*(x5+3)**2- 9

    x6=np.arange(-4, 1, 1)
    y6=1.5*(x6+3)**2-10

    for i in range(1, 7, 1):
        pl.plot(eval(f"x{i}"), eval(f"y{i}"), Color[0]+"-")

    pl.show()

# Vihmavari()











## eval =    строка ---> код

## plt.plot(x, y, linestyle='--', marker='s', color='r', linewidth=2)
##Цвета определяются символами (по первым буквам английских названий цветов): c , m , y , r , g , b, w, k (черный)

##Стиль линии
##„–„ (минус) сплошная линия,
##„—-‘ (два минуса) разрывная линия,
##„:’ (двоеточие) пунктирная линия,
##„–.’ (минус точка)штрих пунктирная.
##Маркеры:
##    „s‟ – квадрат,
##    „o‟ – круг,
##    „p‟ – пятиугольник,
##    „d‟ – ромб,
##    „x‟ – крест,
##    „*‟ – звезда,
##    „+‟ – плюс,
##    „h‟ – шестиугольник.
