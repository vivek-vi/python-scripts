x = eval(input("Enter number of seconds for the conversion in hh:mm:ss format- "))

y = x // 60
z = x % 60

if y > 59:
	h = y // 60
	m = y % 60
	print ('%d seconds = ' % x, h, 'hour and', m, 'minutes', z, 'seconds')
else:
	print ('%d seconds = ' % x, y, 'minutes and', z, 'seconds')