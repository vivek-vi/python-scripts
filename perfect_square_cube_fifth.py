count = 0

for i in range(1, 10001):
	if (i ** 2 < 1001) or (i ** 3 < 1001) or (i ** 5 < 1001):
		count += 1

print ((1000 - count), 'Integres from 1 to 1000 are not perfect squares, perfect cubes or perfect fifth powers.')
