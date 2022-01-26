x = eval(input('Enter length of the box: '))
y = eval(input('Enter width of the box: '))

for i in range(y):
	if i == 0 or i == (y - 1):
		print ('*' * x)
	else:
		print ('*', ' ' * (x - 4), '*')
