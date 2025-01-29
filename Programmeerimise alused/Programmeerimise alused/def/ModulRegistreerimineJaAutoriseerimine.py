## modul
from curses.ascii import isdigit, islower
import random
UsernamesList = []
PasswordsList = []
charsList = ['.',',',':',';','!','_','*','-','+','(',')','/','#','¤','%','&','@']
print(charsList)
def RandomPass():
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    return psword

def CheckPass(psword):
    for x in range(len(psword)):
        if psword[x].isdigit() == True:
            print('1 lvl')
            for x in range(len(psword)):
                if psword[x].isupper() == True:
                    print('2 lvl')
                    for x in range(len(psword)):
                        if psword[x].islower() == True:
                            print('3 lvl')
                            for y in range(len(psword)):
                                if psword[y] in charsList:
                                    print('4 lvl')
                                    return True
    return False
def check_user_in_list(User):
    if User in UsernamesList:
        return False
    else:
        return True