count4 = 0
count9 = 0

for i in range(1, 101):
	if (i ** 2) % 10 == 4:
		count4 += 1
	elif ( i ** 2) % 10 == 9:
		count9 += 1

print ('Squares ends with 4 are: ', count4)
print ('Squares ends with 9 are: ', count9)