x = input('Enter a string: ')
x = x.lower()

for i in x:
	if i in'.,':
		x = x.replace(i,'')

print ('Updated string is', x)
