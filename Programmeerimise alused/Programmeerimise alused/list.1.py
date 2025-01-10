spisok=[]
numbers=[1,2,3,4,5]
abc=['Abc','B','C']
slovo="Programmerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print('1 - Add new letter to list')
    print('2 - extend list\n3-add letter om i- position')
    print('4 - delete element')
    valik=int(input())
    if valik==1:
        a=input('Enter letter')
        slovo_list.append(a)
        print(f'You added {a} new list',slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input('Enter letter, which do you want add')
        i=int(input('Enter number of possition'))
        slovo_list.insert(i-1,a)
        print(slovo_list)
    elif valik==4:
        a=input('Enter letter, which do you want delete')
        n=slovo_list.count(a)
        if n > 0:
            for i in range(n):
                slovo_list.remove(a)
        else:
            print("We don't have that letter")
        print(slovo_list)