charsList = ['.',',',':',';','!','_','*','-','+','(',')','/','#','¤','%','&','@']
psword = input('ps')
def CheckPass(psword):
    for x in range(len(psword)):
        if psword[x].isdigit() == True:
            print('1 lvl')
            if psword[x].isupper() == True:
                print('2 lvl')
                if psword[x].islower() == True:
                    print('3 lvl')
                    for y in range(len(psword)):
                        if psword[y] in charsList:
                            return True
        return False
Test=CheckPass(psword)
print(Test)