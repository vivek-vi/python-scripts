x = eval(input('Enter length in centimeters: '))

if x < 0:
	print ('Invalid length, please provide positive number!')
	
else:
	print ('Length in the inch is: ', (x / 2.54))