x = eval(input("Enter angle between -180 to 180: "))

if x < 0:
	y = abs(x)
	print ("Equivalent angle between 0 & 360 degreee is: ", (180 + y))
else:
	print ("Equivalent angle between 0 & 360 degree is: ", x)