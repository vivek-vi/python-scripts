x = eval(input('Enter the temperature: '))
y = input ('Please provide unit Celcius(C)/Fahrenheit(F): ')

if y == 'F':
	print ('Temperature in Celcius is: ', ((5 / 9) * (x - 32)))
	
elif y == 'C':
	print ('Temperature in Fahrenheit is: ', ((9 / 5) * (x + 32)))
	
else:
	print ('Please enter valid unit alphabet i.e. C/F')