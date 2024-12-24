# Plokkskeemide koostamine
try:
    a, b, h = None, None, None
    a, b, h = float(input('Enter A')), float(input('Enter B')), float(input('Enter H'))
except:
    print('error')
if a is not None and b is not None and h is not None:
    S = (a + b) * h / 2
    print(S)
else:
    print('valiable is empty')

# 1
quantitiesOfNumbers = None
try:
    quantitiesOfNumbers = int(input('Enter quantity of numbers'))
except:
    print('error only int')
x = 0
for x in range(quantitiesOfNumbers):