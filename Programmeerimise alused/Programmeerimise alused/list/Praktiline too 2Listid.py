#1 doesn't work
pfrace = input("enter phrace")
countVowels = 0
countNonVowels = 0
vowels = ['A', 'E', 'I', 'O', 'U']
NonVowels = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
lenpfrace = len(pfrace)
for char in pfrace:
    if char in vowels == True:
        countVowels+=1
        print('vowel')
    elif char in NonVowels == True:
        countNonVowels+=1
        print('notvowel')
# for char in pfrace.upper():
#     if char in vowels():
#         countVowels+=1
#     elif char in NonVowels:
#         countNonVowels+=1
print(countVowels, countNonVowels)
