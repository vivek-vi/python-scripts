x = eval(input('Enter value of x: '))
y = eval(input('Enter value of y: '))
z = eval(input('Enter value of z: '))

swap1 = x
swap2 = z
x = y
y = swap2
z = swap1

print ('We have swapped the numbers as x, y, z with', x,',', y,',', z, 'respectively.')