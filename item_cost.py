x = eval(input('Enter a number of items purchasing: '))

if x < 10:
	print ('Total cost of your purchase is: %d$' % (x * 12))
	
elif 9 < x < 100:
	print ('Total cost of your purchase is: %d$' % (x * 10))
	
else:
	print ('Total cost of your purchase is: %d$' % (x * 7))