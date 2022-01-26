x = eval(input('Enter a number: '))
count = 1
for i in range(1, x + 1):
	count = count * i
	
print ('Factorial of %d is' % x, count)