import random
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
def questioner(name:str, lines:list, congratulations:list, goodluck_list:list):
    numbersOfQuestions = [0,1,2,3,4,5,6,7,8,9]
    count = 0
    for x in range(5):
        Bnumber = False 
        while Bnumber == False:
            QuestionNumber = random.randint(1,11)
            if QuestionNumber in numbersOfQuestions:
                Bnumber = True
                numbersOfQuestions.remove(QuestionNumber)
        Question, Answer = lines[QuestionNumber].split(": ")
        print(name, 'Answer the question. Question NR:',Question)
        answer = input('Enter answer: ').upper()
        # print(Answer)
        if Answer == answer:
            count = count + 1
            # print(count)
    if count >= 3:
        data = [count, name]
        congratulations.append(data)
    else:
        data = [count, name]
        goodluck_list.append(data)
    congratulations.sort(reverse=True)
    return congratulations, goodluck_list
# answer = questioner('Zhan', answer1, congratulations_list, goodluck_list)
# def sortListWithGrade(congratulations_name:list, congratulations_score:list):
#     sortV = sorted(range(len(score)), key=lambda i: score[i], reverse=True)
#     sorted_congratulations_name = [congratulations_name[i] for i in sortV]
#     sorted_congratulations_score = [congratulations_score[i] for i in sortV]
#     return sorted_congratulations_name, sorted_congratulations_score
def write_file(fail:str, wlist:list):
    f = open(fail,'w',encoding="utf-8-sig")
    for row in wlist:
        for item in row:
            f.write(str(item) + '\n')
    f.close()