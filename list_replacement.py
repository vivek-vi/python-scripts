x = eval(input('Enter lists containing numbers between 1 to 12: '))

#replace all of the entries in the list that are greater than 10 with 10
for i in range(len(x)):
	if x[i] > 10:
		x[i] = 10

print(x)