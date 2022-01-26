from random import randint
x = 1
y = 2

for i in range(x, 51):
	z = randint(x, y)
	print ("Random number between %d & %d is: " %(x, y), z)
	if i < 51:
		i += 1
		y += 1
	