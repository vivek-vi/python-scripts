x = eval(input('If the candy is divided evenly among 5 people, how many pieces would be left over? '))
y = eval(input('If the candy is divided evenly among 6 people, how many pieces would be left over? '))
z = eval(input('If the candy is divided evenly among 7 people, how many pieces would be left over? '))


for i in range(1, 200):
	if i % 5 == x:
		if i % 6 == y:
			if i % 7 == z:
				print('Total available candies are: ', i)
				
	
		
 
	