x = eval(input('Enter power of 2: '))
#y = eval(input('Enter number of digits you want: '))

print ('Last digit of 2 power %d is' % x, (( 2 ** x ) % 10))
print ('Last two digit of 2 power %d is' % x, (( 2 ** x ) % 100))
#print ('2 raise to %d is' % x, round( 2 ** x, y))

