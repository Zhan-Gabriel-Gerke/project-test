from random import *
from datetime import date
#1
# nimi = input('What\'s your name?')
# if nimi.isalpha() and nimi.isupper():
#     if nimi == 'JUKU':
#         print('Lahme kinno')
#         try:
#             vanus = int(input(f'kui vana sa oled {nimi}?'))
#             if vanus < 0:
#                 print('viga!')
#             elif vanus <= 6:
#                 print('tasuta')
#             elif vanus < 15:
#                 print('Lastepilet')
#             elif vanus < 65:
#                 print('taispilet')
#             elif vanus < 100:
#                 print('sooduspilet')
#             else:
#                 print('NII PALJU')
#         except:
#             print('error vanus')
#     else:
#         print('Ootan Juku')
# else:
#     print('SEGATUD sone')
#2
#v 1
# try:
#     name1, name2 = input('enter name 1'), input('enter name2')
#     names = ['Den', 'Veronika', 'Zhan', 'Gabriel', 'Gleb', 'Krill', 'Mari']
#     if name1.isalpha() and name2.isalpha():
#         if (name1 in names) and (name2 in names):
#             print('There are neighbors')
#         else:
#             print('They are not neighbors')
#     #     print('today you are sitting together')
#     # else:
#     #     print('today you are not sitting together')
# except:
#     print('error 2 ex v1')
# #v 2
# try:
#     name1, name2 = input('enter name 1'), input('enter name2')
#     if (name1 == 'Zhan' and name2 == 'Gabriel') or (name1 == 'Gabriel' and name2 == 'Zhan'):
#             print('There are neighbors')
#     else:
#         print('They are not neighbors')
#     #     print('today you are sitting together')
#     # else:
#     #     print('today you are not sitting together')
# except:
#     print('error 2 ex v2')
#3
try:
    leight_first_wall = float(input('enter leight of your smalles wall'))
    leight_second_wall = float(input('enter leight of your largerst wall'))
    questionn = input('would you like to do renovation "YES" or "NO"')
    if questionn.upper() == 'YES':
        price_of_renovation_per_m = float(input('Enter the price for square meter'))
        s_of_room = leight_first_wall * leight_second_wall
        print(f'square of room is {s_of_room}')
        price_for_renovation = price_of_renovation_per_m * s_of_room
        print(f'price for renovation will be {price_for_renovation}')
    elif questionn.upper() == 'NO':
        print('ok')
    else:
        print('you wrote not correct value')
except:
    print('error ex3')
#4
try:
    total_price = float(input('enter price'))
    if total_price > 0 and total_price > 700:
        price_with_discount = total_price * 0.7
    else:
        price_with_discount = total_price
    print(f'price will be {price_with_discount}')
except:
    print('error ex4')

#5
try:
    temp_room = float(input('enter temperatul of room'))
    if temp_room > 18:
        print('temp more that 18')
except:
    print('error ex5')

#6
try:
    height = float(input('enter your height'))
    if height < 100:
        print('very short')
    elif height < 150:
        print('short')
    elif height < 175:
        print('average')
    elif height < 190:
        print('long')
    elif height < 220:
        print('who are you ?')
    else:
        print('error')
except:
    print('error ex6')
#7
try:
    height7 = float(input('enter height'))
    sex = input('enter your sex "M or W"')
    if sex.upper() == 'M':
        if height < 100:
            print('very short')
        elif height < 150:
            print('short')
        elif height < 175:
            print('average')
        elif height < 190:
            print('long')
        elif height < 220:
            print('who are you ?')
        else:
            print('error')
    elif sex.upeer() == 'W':
        if height < 80:
            print('very short')
        elif height < 120:
            print('short')
        elif height < 150:
            print('average')
        elif height < 165:
            print('long')
        elif height < 200:
            print('who are you ?')
        else:
            print('error')
except:
    print('error 7')

#8
try:
    answerr = input('would you like to buy groceries "YES" or "NO"')
    if answerr.upper() == "YES":
        question1, question2, question3 = input('1. would you like to buy milk "YES" or "NO"'), input('2. would you like to buy bread "YES" or "NO"'), input('3. would you like to buy eggs "YES" or "NO"')
        if question1.upper() == "YES":
            product1 = randint(1, 10)
        if question2.upper() == "YES":
            product2 = randint(1, 10)
        if question3.upper() == "YES":
            product3 = randint(1, 10)
        total_groceries_price = product1 + product2 + product3
        if product1 > 0:
            print(f'milk {product1} + 22% tax = {product1 * 1.22} Euro')
        if product2 > 0:
            print(f'bread {product2} + 22% tax = {product2 * 1.22} Euro')
        if product3 > 0:
            print(f'eggs {product3} + 22% tax = {product3 * 1.22} Euro')
        print(f'recepe total cost for groceries {total_groceries_price}')
except:
    print('error ex 8')

#9
try:
    AsideSquare, BsideSquare = float(input('Enter first lenght of square')), float(input('Enter second lenght of square'))
    CsideSquare, DsideSquare = float(input('Enter third lenght of square')), float(input('Enter fourth lenght of square'))
    if AsideSquare == BsideSquare and AsideSquare == CsideSquare and AsideSquare == DsideSquare:
        print('all sides are equal')
    else:
        print('all sides aren\'t aqual')
except:
    print('error ex 9')

#10
try:
    mathfun = input('Please enter math function which do you want to calculate "+, -, *, /"')
    num1, num2 = float(input('enter first number')), float(input('enter seconf number'))
    if mathfun == '+':
        sumnum = num1 + num2
    elif mathfun == '-':
        sumnum = num1 - num2
    elif mathfun == '*':
        sumnum = num1 * num2
    elif mathfun == '/' or ':':
        sumnum = num1 / num2
    else:
        print('you wrote wrong math function')
except:
    print('error ex10')

#11 Доделай потом
# try:
#     datebirth = input('Please enter you date of birth"yyyy-mm-dd"')
#     # print(datebirth)
#     todaydate = date.today()
#     # print(todaydate)
#     # birthyear = datebirth[0:4]
#     # print(birthyear)
#     ubelei = todaydate[0:4] - datebirth[0:4]
#     print(ubelei)
#     if ubelei % 5 == 0:
#         print('юбилеййййй')
#     else:
#         print('не юбилей')
# except:
#     print('error ex 11')

#12 
try:
    price_for_product = float(input('Enter price for product in euro\'s'))
    if price_for_product > 10:
        discount = 0.1
    elif price_for_product < 10:
        discount = 0.2
    else:
        print('error')
    print(f'{price_for_product - (price_for_product * discount)} total price')
except:
    print('error ex 12')

#13
try:
    sex = input('enter your sex "M" or "W"')
    if sex.upper == 'M':
        age = int(input('Please enter your age'))
        if age => 16 and age =< 18:
            print('Welcome')
        else:
            print('Sorrt but no')
    elif sex.upper == 'W':
        print('Sorry only mens')
    else:
        print('you wrote wrong answer')
except:
    print('error ex 13')

#14 
