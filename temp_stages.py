x = eval(input('Enter the temperature in Celcius: '))

if x < -273.15:
	print ('Temperature is invalid because it is below absolute zero.')
	
elif x == -273.15:
	print ('Temperature is absolute 0.')
	
elif -273.15 < x < 0:
	print ('Temperature is below freezing.')
	
elif x == 0:
	print ('Temperature is at the freezing point.')
	
elif 0 < x < 100:
	print ('Temperature is in the normal range.')
	
elif x == 100:
	print ('Temperature is at the boiling point.')
	
else:
	print ('Temperature is above the boiling point.')