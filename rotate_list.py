x = eval(input('Enter a lists: '))
y = []

for i in range(0, len(x)):
	y = y + [x[i-1]]


print(y)