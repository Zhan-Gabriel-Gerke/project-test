import random
# from gtts import *
# from os import path, remove, system
country_capital_dict = {}
capiral_country_dict = {}
country = []
# # def write_to_single_file():
# #     with open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\def\Users.Pass.txt', "w", encoding="utf-8") as f:
# #         for x in range(len(UsernamesList)):
# #             TempVariable = f"{UsernamesList[x]}:{PasswordsList[x]}"
# #             f.write(TempVariable + "\n")
# def write_to_single_file():
#     file = open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\dict\Country,Capital.txt')
#     for pairs in country_capital_dict:
#         n = pairs.find(":")
# def file_to_dict():
#     file = open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\dict\Country,Capital.txt','r', encoding = 'utf-8-sig')
#     for line in file:
#         k,v = line.strip('-')
#         country_capital_dict[k]=v
#         capiral_country_dict[v]=k
#         country.append(k)
#     file.close
# # def read_country_capital():
# #     file = open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\dict\Country,Capital.txt')
# #     for line in file:
# #         n = line.find("-")
# #         TempVariableCountry = line[0:n].strip()
# #         TempVariableCaptital = line[n+1:len(line)].strip()
# #         country_capital_dict[TempVariableCountry] = TempVariableCaptital
# #     file.close
# #     return country_capital_dict
# def search(which_dict:dict, Name:str):
#     TrueOrFalse = Name in which_dict
#     if TrueOrFalse == True:
#         answer = which_dict[Name]
#     else:
#         answer = False
#         return answer
# def add_to_dict(which_dict):
#         print("We didn't find . Would you like add it to dictionary")
#         YesOrNo = input('Enter Yes or No').isupper()
#         if YesOrNo == 'YES' or YesOrNo == '1' or YesOrNo == '+':
#             country = input('Enter name of the contry')
#             capital = input('Enter name of the capital')
#             if len(country) == 0 or len(capital) == 0:
#                 answer = 'Error, Variable is empty'
#                 return answer
#             else:
#                 which_dict[country] = capital
#                 answer = 'Thank you for your support'
#                 return answer
# def update_dict_capital(NameOfCountry:str ,RightName:str):
#     country_capital_dict[NameOfCountry] = RightName
# def update_dict_country(NameOfCountry:str, RightName:str):
#     capital = country_capital_dict.pop(NameOfCountry)
#     country_capital_dict[RightName] = capital
# # read_country_capital()
# # AAA = search('Bosnia ja Hertsegoviina')
# # print(AAA)
# def country_capital_test():
#     country_capital_list = list(country_capital_dict)
#     quatityOfCountry = len(country_capital_list)
#     Possible_Options = []
#     count = 0
#     for x in range(quatityOfCountry-1):
#         Possible_Options.append(x)
#     for y in range(10):
#         Random_Variable = random.randint(0,quatityOfCountry-1)
#         for xyx in range(1):
#             if Random_Variable in Possible_Options:
#                 Possible_Options.remove(Random_Variable)
#                 answer = input(f'Capital of {country_capital_list[Random_Variable]} ')
#                 right_answer = country_capital_dict.get(country_capital_list[Random_Variable])
#                 if answer == right_answer:
#                     count = count + 1
#                 else:
#                     print('Your answer: ',answer, 'Right answer: ', right_answer)
#             else:
#                 continue
#         # else:
#         #     Random_Variable = random.randint(0,quatityOfCountry)
#         #     answer = input(f'Capital of  {country_capital_list[Random_Variable]} ')
#         #     right_answer = country_capital_dict.get(country_capital_list[Random_Variable])
#         #     if answer == right_answer:
#         #         count = count + 1
#         #     else:
#         #         print('Your answer: ',answer, 'Right answer: ', right_answer)
#     print(f"Right answers: {count}")
# def text_to_speech(tekst:str,language:str):
#     obj=gTTS(text=tekst,lang=language,slow=False).save("heli.mp3")
#     system("heli.mp3")
def file_to_dict():
    file = open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\dict\Country,Capital.txt','r', encoding = 'utf-8-sig')
    for line in file:
        k,v = line.strip().split('-')
        country_capital_dict[k]=v
        capiral_country_dict[v]=k
        country.append(k)
    file.close
def dict_to_file():
    file = open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\dict\Country,Capital.txt', 'w', encoding='utf-8-sig')
    for k, v in country_capital_dict.items():
        file.write(f"{k}-{v}\n")
    file.close()
def search(Name:str):
    if Name in country_capital_dict:
        answer = country_capital_dict[Name]
    elif Name in capiral_country_dict:
        answer = capiral_country_dict[Name]
    else:
        answer = "We don't have that Country or Capital in our Dictionary"
    print(answer)
def add_to_dict(country:str, capital:str):
    capiral_country_dict[capital] = country
    country_capital_dict[country] = capital
    print(f'The dictionary has been change')
    dict_to_file()
    print(capiral_country_dict)
    print(country_capital_dict)
def change_dict_country(Error_Name:str, Right_Name:str):
    Capital = country_capital_dict.pop(Error_Name)
    del capiral_country_dict[Capital]
    country_capital_dict[Right_Name] = Capital
    capiral_country_dict[Capital] = Right_Name
    dict_to_file()
def change_dict_capital(Error_Name:str, Right_Name:str):
    Country = capiral_country_dict.pop(Error_Name)
    del country_capital_dict[Country]
    country_capital_dict[Country] = Right_Name
    capiral_country_dict[Right_Name] = Country
    dict_to_file()
def country_capital_test():
    capiral_country_list = list(capiral_country_dict)
    country_capital_list = list(country_capital_dict)
    quatityOfCountry = len(country_capital_list)
    Possible_Options = []
    count = 0
    whileCount = 0
    for x in range(quatityOfCountry-1):
        Possible_Options.append(x)
    while whileCount < 5:
        Random_Variable = random.randint(0,quatityOfCountry-1)
        if Random_Variable in Possible_Options:
            Possible_Options.remove(Random_Variable)
            answer = input(f'Capital of {country_capital_list[Random_Variable]} ')
            right_answer = country_capital_dict.get(country_capital_list[Random_Variable])
            if answer == right_answer:
                count = count + 1
            else:
                print('Your answer: ',answer, 'Right answer: ', right_answer)
            whileCount = whileCount + 1
    else:
        Possible_Options = []
        whileCount = 0
        for x in range(quatityOfCountry-1):
            Possible_Options.append(x)
        while whileCount < 5:
            Random_Variable = random.randint(0,quatityOfCountry-1)
            if Random_Variable in Possible_Options:
                Possible_Options.remove(Random_Variable)
                answer = input(f"{capiral_country_list[Random_Variable]} What country capital is this ")
                right_answer = capiral_country_dict.get(capiral_country_list[Random_Variable])
                if answer == right_answer:
                    count = count + 1
                else:
                    print('Your answer: ',answer, 'Right answer: ', right_answer)
                whileCount = whileCount + 1
    print(f"Right answers: {count * 10}%")