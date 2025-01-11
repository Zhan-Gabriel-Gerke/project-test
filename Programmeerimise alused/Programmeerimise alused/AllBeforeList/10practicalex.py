# # ex 1 not ready
# for x in range(15):
#     try:
#         num1 = input('Please enter the number')
#         num1_int = isinstance(num1, int)
#         print(num1_int)
#     except:
#         print('error ex1')

# # ex 2
# while 1:
# 	try:
# 		A = int(input("enter A"))
# 		break
# 	except:
# 		print('error')
# summa = 0
# if A > 0:
# 	for i in range(1, A+1, 1):
# 		summa+=i
# 		print(f'{i}. summ = {summa}')
# print(f"vastus {summa}")

# # ex 3
# p = 1
# for j in range(8):
# 	while 1:
# 		try:
# 			arv = float(input('enter the number'))
# 			break
# 		except:
# 			print('error ex 3')
# 	if arv > 0: 
# 		p*=arv
# 	else:
# 		print('number less that 0')
# 	print(f'{j}. sum total= {p}')
# print(f'final result{p}')

# # ex 4
# for i in range(10, 20, 1):
# 	print(i**2, end=';')
# # ex 5
# try:
#     quatitiesofnumbers = int(input('How many numbers do you want input'))
# except:
#     print('Error ex5')
# count = 0
# for x in range(quatitiesofnumbers):
#     x = float(input('Enter the number'))
#     if x < 0:
#         count =count + x
#         print(count)
# # ex 6
# try:
#     quantitesofnumbers = int(input('How many numbers do you want input'))
# except:
#     print('Error ex 6')
# countp = 0
# countm = 0
# for x in range(quantitesofnumbers):
#     x = float(input('Enter the number'))
#     if x >= 0:
#         countp = countp + 1
#     elif x < 0:
#         countm = countm + 1
# # print(f'- {countm}, + {countp}') ne robit
# # # ex 7
# # ex7a = 0
# # for x in range(21):
# #     inch = 2.5
# #     cm = 1
# #     inch = inch * x
# #     cm = cm * x
# #     print(f'{cm} = {inch}')
# # ex 15
# for i in range(10):
# 	for x in range(1, 10):
# 		print(x, end = ' ')
# 	print(' ')
# # ex 16
# for i in range(10):
# 	for j in range(1, 10):
# 		if i == j:
# 			print(j, end = ' ')
# 		else:
# 			print('0', end= ' ')
# 	print() 