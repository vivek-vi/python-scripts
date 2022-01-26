x = input('Enter a word: ')

reverse_word = x[::-1]

if x == reverse_word:
	print ('Entered word is palindrome!')
else:
	print ('Entered Word is not palindrome!')