import random
questions = []
congratulations_list = []
goodluck_list = []
def read_file(fail:str)->list:
    f = open(fail, 'r', encoding="utf-8-sig")
    #variable = f.read().splitlines()
    #questions.append(variable)
    lines = f.read().splitlines()
    # for row in range(len(lines)):
    #     questions.append(lines[row])
    f.close()
    return lines
ff = r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Fail\kusimused_vastused.txt'
answer1 = read_file(ff)
# print(answer[1])
def questioner(name:str, lines:list):
    numbersOfQuestions = [0,1,2,3,4,5,6,7,8,9]
    QuestionNumber = random.randint(0,9)
    return QuestionNumber
answer = questioner('LLL', answer1)
print(answer)