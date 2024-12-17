#import math
from random import *
count = 0
try:
    levelofmath = int(input('Please enter lelvel complexity pf the math "1 - easy, 2 - medium, 3 - hard"'))
except:
    print('error')
if levelofmath == 1:
    try:
        quantityofex = int(input('Plese enter the quatity of exercise'))
    except:
        print('error')
    print('You chose lever easy (Only integer numbers)')
    for x in range(quantityofex):
        mathOperator = randint(1,2)
        num1, num2 = randint(1,100), randint(1,100)
        if mathOperator == 1:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "+"')
            try:
                answer = None
                answer = int(input('Please enter the answer'))
            except:
                print('Only integer numbers. error 18 line')
            if answer is not None: # Проверяет ввёл ли что-то человек или нет 
                rightanswer = num1 + num2
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        elif mathOperator == 2:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "-"')
            try:
                answer = None
                answer = int(input('Please enter the answer'))
            except:
                print('Only integer numbers. error 32 line')
            if answer is not None:
                rightanswer = num1 - num2
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        else:
            print('error mathOperator 1')
elif levelofmath == 2:
    try:
        quantityofex = int(input('Plese enter the quatity of exercise'))
    except:
        print('error')
    for x in range(quantityofex):
        mathOperator = randint(1,4)
        num1, num2 = randint(100,1000), randint(100,1000)
        if mathOperator == 1:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "+"')
            try:
                answer = None
                answer = int(input('Please enter the answer'))
            except:
                print('Only integer numbers. error 57 line')
            if answer is not None:
                rightanswer = num1 + num2
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        elif mathOperator == 2:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "-"')
            try:
                answer = None
                answer = int(input('Please enter the answer'))
            except:
                print('Only integer numbers. error 73 line')
            if answer is not None:
                rightanswer = num1 - num2
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        elif mathOperator == 3:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "*"')
            try:
                answer = None
                answer = float(input('Please enter the answer'))
            except:
                print('Only numbers. error 89 line')
            if answer is not None:
                rightanswer = num1 * num2
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        elif mathOperator == 4:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "/"')
            try:
                answer = None
                answer = float(input('Please enter the answer with two decimal places '))
            except:
                print('Only numbers. error')
            if answer is not None:
                rightanswer = round(num1 / num2, 2)
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        else:
            print('error mathOperator 2')
elif levelofmath == 3:
    try:
        quantityofex = int(input('Plese enter the quatity of exercise'))
    except:
        print('error')
    for x in range(quantityofex):
        num1, num2, num3, mathOperator = randint(100,1000), randint(100,1000), randint(100,1000), randint(1,4)
        if mathOperator == 1:
            print(f'{num1} : {num2} + {num3}')
            try:
                answer = None
                answer = float(input('Enter answer with two decimal places'))
            except:
                print('Only numbers, Error')
            if answer is not None:
                rightanswer = round(num1 / num2 + num3, 2)
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        elif mathOperator == 2:
            print(f'{num1} * {num2} - {num3}')
            try:
                answer = None
                answer = float(input('Enter answer with two decimal places'))
            except:
                print('Only numbers, Error')
            if answer is not None:
                rightanswer = round(num1 * num2 - num3, 2)
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        elif mathOperator == 3:
            print(f'{num1} + {num2} ** {num3}')
            try:
                answer = None
                answer = float(input('Enter answer with two decimal places'))
            except:
                print('Only numbers, Error')
            if answer is not None:
                rightanswer = round(num1 + num2 ** num3)
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
                print('Only numbers, Error')
        elif mathOperator == 4:
            print(f'{num1} - {num2} ** {num3}')
            try:
                answer = None
                answer = float(input('Enter answer with two decimal places'))
            except:
                print('Only numbers, Error')
            if answer is not None:
                rightanswer = round(num1 - num2 ** num3)
                if rightanswer == answer:
                    print('You are right')
                    count = count + 1
                else:
                    print(f'Wrong, right answer was {rightanswer}')
            else:
                print('Variable is empty')
        else:
            print('error mathOperator 3')
    else:
        print('error levelofmath')
    # try:
    #     quantityofex = int(input('Plese enter the quatity of exercise'))
    # except:
    #     print('error')
    # print()
    # aEx3, bEx3, cEx3 = randint(1,15), randint(1,15), randint(1,15)
    # print(f'quadratic level a = {aEx3}, b = {bEx3}, c = {cEx3}')
    # Dex3 = (bEx3 ** 2) - 4 * aEx3 * cEx3
    # D = float(input('Write D'))
    # if Dex3 > 0:
    #     x1Ex3 =(- bEx3 + math.sqrt(Dex3)) / (2 * aEx3)
    #     x2Ex6 =(- bEx3 - math.sqrt(Dex3)) / (2 * aEx3)
    # elif Dex3 == 0:
    #     xEx6 = -bEx3 / (2 * aEx3)
    # elif Dex3 < 0:
    #     print('net kornei')
    # else:
    #     print('error ex6 D')
    # if D == 0:
    #     try:
    #         answer = float(f'Enter X')
    #     except:
    #         print('error')
else:
    print('error')
print(count)
grade = (count / quantityofex) * 100
print(f'{grade} %')