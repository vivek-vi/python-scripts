x = eval(input('Enter length in feet: '))

units = ['inches', 'yards', 'miles', 'millimeters', 'centimeters', 'meters', 'kilometers']

modifier = [12, 0.333333, 0.000189394, 304.8, 30.48, 0.3048, 0.0003048]

for i in range((len(units)-1)):
	print ('Please enter', (i + 1), 'to convert it in', units[i])

selection = eval(input('Enter valid number: '))

j = selection - 1
print ('Converted value is: ', modifier[j]*x)