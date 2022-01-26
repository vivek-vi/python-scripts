x = eval(input('Enter first list of integers: '))
y = eval(input('Enter second list of integers with same size as first: '))

z = []

for i in range(len(x)):
	z = z + [x[i] + y[i]]
	
print('Summation lists is:', z)