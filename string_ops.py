x = input('Enter a string/message: ')

print ('Total number of characters in the string are:', len(x))
print (x * 10)
print (x[0], 'is the first character of the string.')
print (x[:3], 'are initial 3 characters in the string.')
print (x[-3:], 'are last 3 characters in the string.')
print (x[::-1], 'reverse characters in the string.')

new_word = x
if x[7].isalpha():
	print (x[7], 'is a 7\'th character in the string.')
else:
	print ('Seventh character is not a letter.')

for c in range(len(x)):
	if c == 0 or c == (len(x) - 1):
		new_word = new_word.replace(x[c], '')

print (new_word, 'This is after removing first & last character.')

print (x.upper())
replace_word = x
for c in range(len(replace_word)):
	if replace_word[c] == 'a':
		replace_word = replace_word.replace('a', 'e')

print ('Word after replacing a with e: ', replace_word)

space_word = x

for i in space_word:
	if i.isalpha():
		space_word = space_word.replace(i, '')
	else:
		print (i, end='')