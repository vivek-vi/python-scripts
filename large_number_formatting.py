x = input('Enter a large number: ')
y = len(x)
new_x = ''
for i in range(len(x),-1, -1):
	print(i, 'i')
	print(len(new_x), 'length of new_x at start')
	if len(new_x) % 3 == 0 and len(new_x) != 0:
		new_x = x[i-1] + ',' + new_x
		print(new_x, 'inside if')
	elif i > 0:
		new_x = x[i-1] + new_x
		print(new_x, 'inside else')

print (new_x)
	