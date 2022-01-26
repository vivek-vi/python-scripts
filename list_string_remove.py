x = eval(input('Enter lists with strings: '))

y = []
#Create a new list that consists of those strings with their first characters removed
for i in x:
	y = y + [i[1:]]
	
print(y)


