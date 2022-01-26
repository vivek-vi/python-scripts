x = eval(input('Enter a number: '))
count = 0
for i in range (2, x):
	if x % i == 0:
		if x % ( i ** 2) == 0 and (i ** 2) != x:
			count += 1
			print (x, 'is not a squarefree number and divisible by', i,'and it\'s square.', i ** 2)

if count == 0:
	print (x, 'is a squarefree number.')

