x = input('Enter your full name in lower case: ')
x = x.lower()
alt = ''
for i in range(len(x)):
	#print(i)
	if i == 0 or x[i - 1] == ' ':
		alt = alt + x[i].upper()
	elif x[i] == ' ':
		alt = alt + x[i]
	else:
		alt = alt + x[i]
		
print('Your formatted name is: ', alt)