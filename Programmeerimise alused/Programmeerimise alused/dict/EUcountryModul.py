country_capital_dict = {}
# def write_to_single_file():
#     with open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\def\Users.Pass.txt', "w", encoding="utf-8") as f:
#         for x in range(len(UsernamesList)):
#             TempVariable = f"{UsernamesList[x]}:{PasswordsList[x]}"
#             f.write(TempVariable + "\n")
def read_country_capital():
    file = open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\dict\Country,Capital.txt')
    for line in file:
        n = line.find("-")
        TempVariableCountry = line[0:n].strip()
        TempVariableCaptital = line[n+1:len(line)].strip()
        country_capital_dict[TempVariableCountry] = TempVariableCaptital
    file.close
    return country_capital_dict
def search(Name:str):
    TrueOrFalse = Name in country_capital_dict
    if TrueOrFalse == True:
        answer = country_capital_dict[Name]
        return answer
    else:
        print("We didn't find that Country. Would you like add it to dictionary")
        YesOrNo = input('Enter Yes or No').isupper()
        if YesOrNo == 'YES' or YesOrNo == '1' or YesOrNo == '+':
            country = input('Enter name of the contry')
            capital = input('Enter name of the capital')
            if len(country) == 0 or len(capital) == 0:
                answer = 'Error, Variable is empty'
                return answer
            else:
                country_capital_dict[country] = capital
                answer = 'Thank you for your support'
                return answer
# def update_dict(Name:str, type:str)
read_country_capital()
# AAA = search('Bosnia ja Hertsegoviina')
# print(AAA)