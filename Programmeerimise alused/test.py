import math
def quadurav(a:int, b:int, c:int):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = ((-1 * b) + math.sqrt(D)) / (2 * a)
        x2 = ((-1 * b) - math.sqrt(D)) / (2 * a)
        print(D)
        print(x1, x2)
    elif D == 0:
        x = (-1 * b) / (2 * a)
        print(x)
    elif D < 0:
        print('Wrong example')
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
quadurav(a, b, c)
