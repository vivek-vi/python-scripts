count = 0
second_highest = 0
highest = 0
lowest = 100
second_lowest = 100
invalid = 0

for i in range (1, 11):
	x = eval(input('Enter your test scores: '))
	count += x
	if x < second_lowest:
		if x <= lowest:
			lowest = x
		else:
			second_lowest = x
			
	if x > second_highest:
		if x >= highest:
			highest = x
		else:
			second_highest = x
	if x > 100:
		invalid += 1

if invalid > 0:
	print ('Warning!! You have entered value greater than 100!!')
			
print (highest, ': highest score\n',lowest, ': lowest score\n',(count / 10), ': average score\n',\
second_highest, ': second highest score\n',((count-(lowest+second_lowest))/8),\
': average without last 2 lowest scores.', sep='')
			
	