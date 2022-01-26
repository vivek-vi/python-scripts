x = input('Enter a word & will redesign with alternate caps: ')
x = x.upper()
y = ''
for i in range(len(x)):
	if i % 2 == 0:
		#print (x[i])
		y = y + x[i].lower()
	else:
		y = y + x[i]

print(y)