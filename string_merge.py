x = input('Enter first string: ')
y = input('Enter second string with same length as of first: ')
new_string = ''
if len(x) != len(y):
	print ('You have entered different length strings....doom!')

else:
	for i in range(len(x)):
		new_string = new_string + x[i] + y[i]
	print(new_string)
