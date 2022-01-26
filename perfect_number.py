for i in range(1, 10001):
	count = 0
	for n in range(1, i):
		if i % n == 0:
			count = count + n
	if count == i:
		print(i, 'is a perfect number!')