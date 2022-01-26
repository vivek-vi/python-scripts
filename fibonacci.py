x = eval(input("How many fibonacci numbers to print? "))

a = 1
b = 1
result = a + b
print (a, end = ',')
print (b, end = ',')

for i in range(2, x):
	result = a + b
	b = a
	print (result, end = ',')
	a = result
	
	
	
	
	
	