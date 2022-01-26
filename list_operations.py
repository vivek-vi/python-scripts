x = eval(input('Enter a list of integers: '))

#Print the total number of items in the list.
print('You have entered total %d number of items in the list' % len(x))

#Print the last item in the list.

print (x[-1], 'is the last item from the provided list.')

#Print the list in reverse order.

x.reverse()

print ('List in reverse order:', x)

#Print Yes if the list contains a 5 and No otherwise.

if 5 in x:
	print ('Cool! your list contains magic number 5!')
else:
	print ('Your list doesn\'t contains magic number 5' )
	
#Print the number of fives in the list.

print ('Number of fives in the lists: ', x.count(5))

#Remove the first and last items from the list, sort the remaining items, and print the result.

del x[0]
del x[-1]
x.sort()
print ('Your list post removing first & last element:', x)

#Print how many integers in the list are less than 5.
count = 0
for i in x:
	if i < 5:
		count += 1
print ('There are %d integers that are less than 5' % count)