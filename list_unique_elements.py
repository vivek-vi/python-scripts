x = eval(input('Enter a list & we will make it\'s items unique: '))
new = []
for i in x:
	if i not in new:
		new = new + [i]

print(new)