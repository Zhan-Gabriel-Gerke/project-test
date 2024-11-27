from calendar import *
from datetime import *

#1
#Функции day(), month(), year() используются для получения параметров дня, месяца и года из класса date.
#Вычислите, сколько дней осталось до конца месяца и до конца года.
tana=date.today()
tanaf=date.today()

print(f'tere tana on{tanaf}')
d=tana.day
m=tana.month
y=tana.year
print(d, m, y)
# JANUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER = 31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
# if y % 4 == 0:
#     FEBRUARY = 29
# else:
#     FEBRUARY = 28
novP= monthrange(2024,11)[1]
detsP= monthrange(2024,12)[1]
jaak=detsP + novP - d
jaak2=novP-d
print(f'aasta loppuni on {jaak}')
print(f'aasta kuu on {jaak2}')
#2
# программу для указанной операции 3 + 8 / (4 - 2) * 4 для ответа?
#+Как влияет использование/неиспользование скобок на работу?
#+Экспериментируйте с различными комбинациями параллельно и включайте пояснительный текст, чтобы вывод был понятен.
answer0 = 3 + 8 / (4 - 2) * 4
answer1 = (3 + 8) / (4 - 2) * 4
answer2 = 3 + (8 / (4 - 2)) * 4
answer3 = (3 + 8 / (4 - 2)) * 4
print(answer0, answer1, answer2, answer3)

#3
#Внутри квадрата находится круг. Радиус круга равен R.
#Найдите площадь квадрата, периметр квадрата, площадь круга, периметр круга и выведите их на экран.

try: # всё ок
    R = float(input('enter R of circle'))
    Sk=pi*R**2
except: # что-то не правильно
    print('error')
