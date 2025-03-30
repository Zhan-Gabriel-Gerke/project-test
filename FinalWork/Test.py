from dbquery import *
from TkinterFile import *
import random
def randomPassword():
    Alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    Numbers = ['1','2','3','4','5','6','7','8','9','0']
    Symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-']
    password = '.'
    for x in range(10):
        from1to3 = random.randint(1,3)
        if from1to3 == 1:
            random_var = random.randint(1, len(Alphabet)-1)
            var = Alphabet[random_var]
            password = password + var
        elif from1to3 ==2:
            random_var = random.randint(1, len(Numbers)-1)
            var = Numbers[random_var]
            password = password + str(var)
        elif from1to3 ==3:
            random_var = random.randint(1, len(Symbols)-1)
            var = Symbols[random_var]
            password = password + var
    password = password[1:]