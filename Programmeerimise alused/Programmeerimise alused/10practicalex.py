# ex 1
#num1 = float(input('Please enter the number'))
# ex 2
while 1:
	try:
		A = int(input("enter A"))
		break
	except:
		print('error')
summa = 0
if A > 0:
	for i in range(1, A+1, 1):
		summa+=i
		print(f'{i}. summ = {summa}')
print(f"vastus {summa}")

# ex 3
p = 1
for j in range(8):
	while 1:
		try:
			arv = float(input('enter the number'))
			break
		except:
			print('error ex 3')
	if arv > 0: 
		p*=arv
	else:
		print('number less that 0')
	print(f'{j}. sum total= {p}')
print(f'final result{p}')

# ex 4
for i in range(10, 20, 1):
	print(i**2, end=';')
# ex 15
for i in range(10):
	for x in range(1, 10):
		print(x, end = ' ')
	print(' ')
# ex 16
for i in range(10):
	for j in range(1, 10):
		if i == j:
			print(j, end = ' ')
		else:
			print('0', end= ' ')
	print() 