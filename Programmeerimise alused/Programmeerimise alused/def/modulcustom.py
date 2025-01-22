from random import *
def summa3(arv1:int,arv2:int,arv3:int)->int:
    """ Tagastab kolme taisarvu summa

    :param int arv1: Esimene number  
    :param int arv2: Teine number:
    :param int arv3: Kolmas number:
    :param int arv4: Neljas number:
    :rtype: int

    """
    summa=arv1+arv2+arv3
    return summa
def arithmetic(a:float,b:float,t:str)->any:
    """Lihtne kalkulaator.
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv1
    :param float b: arv2
    :param srt t: atitmeetiline tehing
    :rtype var Määramata tüüp(float or str)
    """
    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tehe"
    return vastus
#2
def is_year_leap(aasta:int)->bool:
    """Liigasta leidmine
    Tagastab True, kui liigasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :trype: bool tagastab loogilises formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
#3
def square(a:float)->any:
    """
    Test
    """
    S=a**2
    P=4*a
    d=(2)**(1/2)*2
    return S,P,d

def season(NumberOfMonth:int)->str:
    """
    """
    if NumberOfMonth == 1 or NumberOfMonth == 2 or NumberOfMonth == 12:
        NameOfMonth = "Winter"
    elif NumberOfMonth == 3 or NumberOfMonth == 4 or NumberOfMonth == 5:
        NameOfMonth = "Spring"
    elif NumberOfMonth == 6 or NumberOfMonth == 7 or NumberOfMonth == 8:
        NameOfMonth = "Summer"
    elif NumberOfMonth == 9 or NumberOfMonth == 10 or NumberOfMonth == 11:
        NameOfMonth = "Autumh"
    else:
        NameOfMonth = "Error"
    return NameOfMonth

def bankdeposit(money:float, years:int)->float:
    for x in range(years):
        money = money * 1.1
    return money

def is_prime(a=randint(0,1000))-> bool:
    print(a)
    v=True
    for i in range(2,a):
        if a%i==0:
            v = False
    # if a > 1:
    #     for x in range(a):
    #         x = x + 1 
    #         if a / a:
    #             boolnumber = True
    #         if a % x == 0:
    #             boolnumber = False
    return v

def date(day:int, month:int, year:int)->bool:
