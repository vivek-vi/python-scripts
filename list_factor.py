x = eval(input('Enter an integer to find the factor: '))
#print(x,'x')
y = []

for i in range(1, x + 1):
#	print(i, 'i')
	if x % i == 0:
		y = y + [i]

print('List of factorials are:', y)