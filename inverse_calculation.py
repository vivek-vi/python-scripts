from math import *
count = 0
x = eval(input('Enter a number: '))

for i in range(1, x + 1):
	count = count + (1 / i)
	
print ('(1+1/2+1/3..)-ln(%d)' % x, '=', (count - log(x)))