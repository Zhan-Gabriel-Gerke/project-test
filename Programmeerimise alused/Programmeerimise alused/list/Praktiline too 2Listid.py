# for marina's solution
import string
#1 Mine
print('English Alphabet')
pfrace = None
try:
    pfrace = input("enter phrace").upper()
except:
    pass
if pfrace is not None:
    countVowels = 0
    countNonVowels = 0
    countChar = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    NonVowels = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    lenpfrace = len(pfrace)
    for quantitychar in range(lenpfrace):
        if pfrace[quantitychar] in vowels:
            countVowels+=1
        elif pfrace[quantitychar] in NonVowels:
            countNonVowels+=1
        else:
            countChar+=1
    print(f'Vowels: {countVowels}, NonVowels: {countNonVowels}, Char: {countChar}')
else:
    print('ERROR Variable is empy')
# for char in pfrace:
#     if char in vowels == True:
#         countVowels+=1
#         print('vowel')
#     elif char in NonVowels == True:
#         countNonVowels+=1
#         print('notvowel')
# for char in pfrace.upper():
#     if char in vowels():
#         countVowels+=1
#     elif char in NonVowels:
#         countNonVowels+=1
#2 Mine Добавь чтобы можно было по имя вводить и менять а не только номер
Names = []
for x in range(5):
    Name = None
    try:
        Name = input('Enter Name')
    except:
        pass
    Names.append(Name)
    if not Name: # Смотрит пустая ли строка
        print('Variable is empty')
print(Name, 'Last name in the list')
Names.sort()
print(Names)
YorN = None
while YorN is None:
    AnswerYN = input('Do you want change list "Yes or No"').upper()
    if len(AnswerYN) >= 1:
        YorN = AnswerYN
    else:
        print('You didn\'n write ansver')
if YorN == 'YES' or YorN == 'Y' or YorN == 'YE' or YorN == 'ES' or YorN == '1' or YorN == 'TRUE' or YorN == '+':
    print(Names)
    NumberOfName = None
    ReplaceName = None
    while NumberOfName is None:
        try:
            NumberOfName = int(input('''Please enter the number of 
                                        record which you want replace
                                        PS.  decrease for 1 1 '''.strip()))# спроси про пробелы
        except:
            print('ERROR Variable is empty')
            continue
    while ReplaceName is None:
        try:
            ReplaceNameTest = input('Please enter the name which you want add')
        except:
            print('ERROR Variable is empty')
            continue
        if len(ReplaceNameTest) >= 1:
            ReplaceName = ReplaceNameTest
    print(NumberOfName)
    NumberOfName = NumberOfName - 1
    print(NumberOfName)
    Names.pop(NumberOfName)
    Names.insert(NumberOfName, ReplaceName)
    print(Names, 'The list has been changed')
else:
    print('OK')
#2.2
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
opilasedWithoutDublicates = []
quantitynames = len(opilased)
print(opilased)
for x in range(quantitynames):
    if opilased[x] in opilasedWithoutDublicates:
        pass
    else:
        opilasedWithoutDublicates.append(opilased[x])
        print(opilasedWithoutDublicates)
#2.3
AgeList = ['10','18','20','25','29','30','38','40','65']

#1 Marina's Solution
# vokaali = ['a', 'e', 'u', 'o', 'i']
# konsanati="qwrtypsdfghjklzxcvbnm"
# markid=string.punctuation #!"#$%&'()*+,-./:;
# while True:
#     v=k=m=t=0
#     tekst = input("Sisesta mingi tekst: ").lower()
#     if tekst.isdigit():
#         break
#     else:
#         tekst_list = list(tekst)
#         print(tekst_list)# 'p', 'r'
#         for taht in tekst_list:
#             if taht in vokaali:
#                 v+=1
#             elif taht in konsanati:
#                 k+=1
#             elif taht in markid:
#                 m+=1
#             elif taht == " ":
#                 t+=1
#     print('Vookali',v)
#     print('Konsonanti',k)
#     print('Markid',m)
#     print('Tuhikud',t)
#2 Marina's Solution
nimed = []
for i in range(5):
    nimi = input(f'{i+1}.Nimi: ')
    nimed.append(nimi)
print('Enne sorteerimist:')
print(nimed)
nimed.sort()
print('Sorteerimise parast:')
print(nimed)
print(f'Viimasena lisatud nimi on: {nimi}')
v = input('Kas muudame nimeid?: ').lower()
if v =='jah':
    v=input('Nimi voi positsiion: N/P').upper()
    if v=="P":
        print('Sisesta nimi asukoht')
        v=int(input())
        uus_nimi = input('Uus nimi: ')
        nimed[v-1]=uus_nimi
        print(nimed)
    else:
        print('Sisesta nimi')
        vana_nimi=input('Vana nimi: ')
        v=nimed.index(vana_nimi)
        uus_nimi = input('Uus nimi: ')
        nimed[v]=uus_nimi
    print(nimed)
#1
dubulta = list(set(nimed))
print(dubulta)
#2