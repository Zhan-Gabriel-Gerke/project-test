from TarkvaraarendajavastuvottModul import *
questions = []
congratulations_name = []
congratulations_score = []
goodluck_list = []
score = []
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
for interviews in range(howMany):
    name = input('Enter name of person')
    testVar = questioner(name, questionsVar, congratulations_name, congratulations_score, goodluck_list)
print(congratulations_name, congratulations_score)
print(goodluck_list)