#1
print('English Letters')
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
#2
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
YesorNo = None
while YesorNo is None:
    try:
        YesorNo = input('Do you want change list "Yes or No"').upper()
    except:
        pass
#    if YesorNo is not None:
if YesorNo == 'YES' or 'Y' or 'YE' or 'ES' or '1' or 'TRUE' or '+':
    print(Names)
    NumberOfName = None
    while NumberOfName is None:
        try:
            NumberOfName = int(input('Please enter the number of record which you want replace'))
            ReplaceName = input('Please enter the name which you want add')
        except:
            print('ERROR Variable is empty')
            continue
    Names.pop(NumberOfName + 1)
    Names.insert(NumberOfName + 1, ReplaceName)
    print(Names, 'The list has been changed')
else:
    print('OK')