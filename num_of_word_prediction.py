x = input('Enter a statement: ')
count = 0
for i in x:
	print (i)
	if i == ' ':
		count = count + 1

print ('There are total %d words in your statement' % (count+1))