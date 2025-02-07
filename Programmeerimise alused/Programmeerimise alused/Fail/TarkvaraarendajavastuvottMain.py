while 1:
    try:
        quantityofInterview = int(input('Enter how many interviews do you want to do'))
    except:
        print('Error')
    if quantityofInterview < 5:
        print('Min 5 interviews')
    else:
        break

# for x in range(quantityofInterview):
#     name = input('Enter name of candidate')
#     f = open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Fail\kusimused_vastused.txt', 'r', encoding ='utf-8-sig')
#     questions_answers = []
#     for row in f:
#         questions_answers.append(row.strip())
#     f.close()
#     print(questions_answers)