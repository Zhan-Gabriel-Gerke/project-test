UsernameList = [1,2,3]
PasswordsList = ['One', 'Two', 'Three']
def write_to_single_file(fail:str, UsernameList:list, PasswordsList:list):
    TempList = []
    fail=open(fail,"w", encoding="utf-8")
    for x in range(len(UsernameList)):
        TempVariable = str(UsernameList[x])+':'+str(PasswordsList[x])
        fail.write(TempVariable+"\n")
    fail.close
write_to_single_file(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\def\Users.Pass.txt', UsernameList, PasswordsList)
