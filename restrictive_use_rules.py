x = input('Enter a string that contains letter "a": ')
x = x.lower()

## Letter check without in operator, we can use 'if' but exception can't handled using else statement.
## So using 'try' & 'except' block.

try:
	x.index('a')
	print ('Great your entered string has letter "a"!')
except ValueError:
	print ('Sorry! entered string doesn\'t contains letter "a".')
	
## count without count method

occurances = 0

for i in x:
	if i == 'a':
		occurances = occurances + 1

print ('Letter a is repeated %d times in provided string' % occurances)

## Calculate index of first occurance of letter 'a' without index method.

absence = 0
present = 0
first = 0
for i in range(len(x)):
	if x[i] == 'a' and first == 0:
		print ('Index of first letter \'a\' in provided string is:', i)
		first = first + 1
	else:
		absence = absence + 1

if absence == 0:
	print ('Letter \'a\' is not present in the given string.')
