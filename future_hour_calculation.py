x = eval(input('Enter hour between 1 & 12: '))
y = eval(input('How many hours we should ahead: '))
print ('New hour: ', (x + y) % 12, 'o\'clock')