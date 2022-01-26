x = input('Enter a word that contains "a" & will split it into 2: ')
count = 0
for i in x:
	if i == 'a' and count == 0:
		#print(i)
		position = x.index(i)
		#print(position)
		print (x[:(position+1)])
		print (x[(position+1):])
		count = count + 1