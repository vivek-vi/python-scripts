x = input('Enter a word: ')
x = x.lower()
count = 0
for i in x:
	if i in 'aeiou':
		count = count + 1

if count != 0:
	print ('Your entered word contains vowels!')

else:
	print ('Your entered word doesn\'t have vowels.')
		