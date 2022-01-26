from random import randint
x = []
for i in range(20):
	x = x + [randint(1,100)]
	
#Print the list.

print (x)

#Print the average of the elements in the list.

print('Average of the elements is:', sum(x) / len(x))

#Print the largest and smallest values in the list.

print ('Largest number in the list is:', max(x))
print ('Smallest number in the list is: ', min(x))

#Print the second largest and second smallest entries in the list

x.sort()

print ('Second largest number in the list is:', x[-2])
print ('Second smallest number in the list is:', x[1])

#Print how many even numbers are in the list.

count = 0

for i in x:
	if i % 2 == 0:
		count += 1
		
print ('List has %d even numbers' % count)