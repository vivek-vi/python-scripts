from random import randint

x = randint(1, 10)
y = eval(input('Guess a number from 1 to 10: '))

if x == y:
	print ('Yay! you guess perfectly!')
	
else:
	print ('Your guess is incorrect! and magic number is ', x)