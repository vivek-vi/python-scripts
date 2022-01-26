x = input('Enter any mathematical formualaes: ')
open = 0
close = 0
for i in x:
	if i == '(':
		open = open + 1
	elif i == ')':
		close = close + 1


if open == close:
	print ('Parenthesis are matched.')
else:
	print ('Please check the missing parenthesis.')
