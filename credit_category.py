x = eval(input('Enter number of taken credits: '))

if x < 24:
	print ('Student is a freshman.')
	
elif x < 54:
	print ('Student is a sophomore.')
	
elif x < 84:
	print ('Student is a junior.')
	
else:
	print ('Student is senior.')