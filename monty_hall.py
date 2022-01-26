from random import randint
correct = 0
wrong = 0
correctswitch = 0
incorrectswitch = 0
idle = 0
for x in range(5):
	prize = randint(1, 3)
	#print (prize)
	x = eval(input('Enter door number(1/2/3) which has prize: '))
	if prize == 1:
		if x == 1:
			y = input('Door 2 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				wrong = wrong + 1
				incorrectswitch = incorrectswitch + 1
			else:
				correct = correct + 1
	
				
		elif x == 2:
			y = input('Door 3 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				correct = correct + 1
				correctswitch = correctswitch + 1
			else:
				wrong = wrong + 1
		else:
			y = input('Door 2 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				correct = correct + 1
				correctswitch = correctswitch + 1
			else:
				wrong = wrong + 1
	
	if prize == 2:
		if x == 1:
			y = input('Door 3 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				correct = correct + 1
				correctswitch = correctswitch + 1
			else:
				wrong = wrong + 1
		elif x == 2:
			y = input('Door 1 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				wrong = wrong + 1
				incorrectswitch = incorrectswitch + 1
			else:
				correct = correct + 1
		else:
			y = input('Door 1 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				correct = correct + 1
				correctswitch = correctswitch + 1
			else:
				wrong = wrong + 1
				
			
	if prize == 3:
		if x == 1:
			y = input('Door 2 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				correct = correct + 1
				correctswitch = correctswitch + 1
			else:
				wrong = wrong + 1
		elif x == 2:
			y = input('Door 1 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				correct = correct + 1
				correctswitch = correctswitch + 1
			else:
				wrong = wrong + 1
		else:
			y = input('Door 1 is empty; do you want to switch your choice?Y/N: ')
			if y == 'Y':
				wrong = wrong + 1
				incorrectswitch = incorrectswitch + 1
			else:
				correct = correct + 1

print ('Great! count of correct guess %d & incorrect are %d' % (correct, wrong))
print ('You made right choice of switch %d time & %d switches are wrong' % (correctswitch, incorrectswitch))
print ('Also you made great decision of not to switch %d times that was correct' % (correct - correctswitch))			
		