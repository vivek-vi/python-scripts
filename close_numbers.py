x = eval(input('Enter first number: '))
y = eval(input('Enter second number: '))

if ((x + 0.001) == y) or ((x - 0.001) == y):
	print ('Close numbers.')
	
else:
	print ('Not close numbers.') 