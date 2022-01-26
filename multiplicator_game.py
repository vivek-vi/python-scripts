from random import randint
correct = 0
wrong = 0
for i in range(1, 11):
	x = randint(1, 10)
	y = randint(1, 10)
	print ('%d * %d' % (x, y))
	z = eval(input('What is answer for above expression: '))
	if (x * y) == z:
		print ('You are right!')
		correct = correct + 1
	else:
		print ('You are wrong & correct answer is: ', (x * y))
		wrong = wrong + 1
		
print ('Great! you have given %d correct answers & %d wrong answers.' % (correct, wrong))