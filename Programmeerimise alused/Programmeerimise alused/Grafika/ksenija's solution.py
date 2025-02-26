from turtle import color
from matplotlib.typing import MarkerType
import numpy as np #x=[min, max]
import matplotlib.pyplot as pl

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
