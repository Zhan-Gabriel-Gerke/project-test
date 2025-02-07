from TarkvaraarendajavastuvottModul import *
questions = []
congratulations = []
goodluck_list = []
while 1:
    try:
        howMany = int(input('Enter how many interviews do you want to do'))
    except:
        print('Error')
    if howMany < 5:
        print('Min 5 interviews')
    else:
        break
filePath = r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Fail\kusimused_vastused.txt'
questionsVar = read_file(filePath)
while 1:
    for interviews in range(howMany):
        name = input('Enter name of person')
        if len(name) == 0:
            print('You wrote enmpy line ,The loop has restarted')
            break
        testVar = questioner(name, questionsVar, congratulations, goodluck_list)
    else:
        break   
congratulationsFail = r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Fail\vastuvoetud.txt'
write_file(congratulationsFail, congratulations)
goodluckFail = r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Fail\eisoobi.txt'
write_file(goodluckFail, goodluck_list)