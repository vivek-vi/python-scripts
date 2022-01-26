from random import randint
count = 0
for i in range(5):
	x = randint(1, 10)
	y = eval(input('Guess a number from 1 to 10: '))
	if x == y:
		print ('Yay! You guess correctly & earned 10 points!')
		count = count + 10
	else:
		print ('Oops! your guess is incorrect & loose 1 point!', 'Number was', x,'Try Again!')
		count = count - 1

print ('You earned total %d points' % count)
		