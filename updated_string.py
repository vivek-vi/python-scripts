x = input('Enter your magic word: ')

for i in range(len(x)):
	if i == 1:
		x = x.replace(x[i], '*', 1)

print ('New string world be ', x, '!!!', sep = '')