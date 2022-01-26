x = eval(input('Enter height of the diamond: '))

for i in range(x):
	if i == 0 or i == (x - 1):
		print (' ' * (x // 2), '*', sep='')
	elif i == ( x // 2):
		print ('*' * x)
	elif i == ((x // 2) - ((x // 2) - i)) or i == ((x // 2) + ((x // 2) + i)):
		print (' ' * ((x // 2) - i), '*' * ((x // 2) + i), sep='')
	#elif i == ((x // 2) - 1) or i == ((x // 2) + 1):
	else:
		print (' ', '*' * (x - 2), sep='')