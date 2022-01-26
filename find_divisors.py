x = eval(input('Enter a number & we will provide all of it\'s divisors: '))

for i in range(1, (x + 1)):
	if x % i == 0:
		print ('Enter number is divisible by', i)
		