import numpy as np # x=[min,max]
import matplotlib.pyplot as plt
def kitt():
    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.3,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-9.5,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    #Создание окна
    plt.figure(facecolor='lightgreen')
    plt.title('Vaal')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)#Чтобы сетка была
    ax=plt.axes()
    ax.set_facecolor("lightblue")
    colors=['c', 'm', 'y', 'r', 'g', 'b', 'w', 'k', 'k', 'k']
    #Рисуем
    for i in range(1,11):
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),colors[i-1]+"-*")
    plt.show()
def otsti():
    x1=np.arange(-9,-0.5,0.5)
    y1=(-1/16)*(x1+5)**2+2
    x2=np.arange(1,9.5,0.5)
    y2=(-1/16)*(x2-5)**2+2
    x3=np.arange(-9,-0.5,0.5)
    y3=1/4*(x3+5)**2-3
    x4=np.arange(1,9.5,0.5)
    y4=1/4*(x4-5)**2-3
    x5=np.arange(-9,-5.5,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9.5,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1.5,0.5)
    y7=(-0.5)*x7*x7+1.5
    plt.figure(facecolor='lightgreen')
    plt.title('Vaal')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)#Чтобы сетка была
    ax=plt.axes()
    ax.set_facecolor("lightblue")
    colors=['c', 'm', 'y', 'r', 'g', 'b', 'w']
    #Рисуем
    for i in range(1,8):
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),colors[i-1]+"-*")
    plt.show()
