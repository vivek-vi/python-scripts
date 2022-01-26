x = eval(input('Enter a number: '))
count = 0
for i in range (2, x):
	if x % i == 0:
		count = count + i
		print(i, 'is divisor of %d' % x)
		
print ('Count of all divisors of %d are' % x, count)