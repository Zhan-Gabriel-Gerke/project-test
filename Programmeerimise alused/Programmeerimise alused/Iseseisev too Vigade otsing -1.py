#3 9, 12, 4.24
## 5 4, 20.0, 18.0, 6.4
### 10, 20.0, 314.16, 62.83
from math import * # тут местами слова поменяли
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) # тут float не было
if a != 3:
    print('sorry you can enter only 3')
    exit()
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)# тут не те скобки были
di = a * sqrt(2)#math не нужен, * не было
print(di)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")# лишняя сокбка
b=float(input("Sisesta ristküliku 1. külje pikkus => "))# float потерялся 
c=float(input("Sisesta ristküliku 2. külje pikkus => "))# float потерялся
if b != 5 and c != 4:
    print('sorry you can enter only 5 and 4')
    exit()
S=b*c
print('Ristküliku pindala', S)# ' не было
P=2*(b+c) # * не было
print("Ristküliku ümbermõõt", P)
di = sqrt(b**2+c**2) # убрал math и добавил *
print("Ristküliku diagonaal", round(di, 2)) # ) не было ну и 2 в округление поставил
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => '))# float не было и много '
if r != 10:
    print('sorrt you can enter only 10')
    exit()
d=2*r# * не было
print("Ringi läbimõõt", d)# , не было
S=pi*r**2 # после pi () лишние, * не хватало для возведения в степерь
print("Ringi pindala", round(S, 2))# 2 в округление добавил
C=2*pi*r# * не было, после pi () лишние
print("Ringjoone pikkus", round(C, 2))# ) не было, 2 в округление добавил