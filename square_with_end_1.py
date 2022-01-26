count = 0
for i in range(1, 101):
	if (i ** 2) % 10 == 1:
		count += 1
		
print (count, 'numbers are having square by ending 1 between 1 & 100.')