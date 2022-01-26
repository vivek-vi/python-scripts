def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ') # split function separate the words by identifying the defined separator
	# In this case separator is 'space' defined within single quote. 
	return words
	
def sort_words(words):
	"""Sort the words."""
	return sorted(words) # sorted function does the alphabetic sorting of the provided input words.
	
def print_first_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0) # pop will pick the word positioned at 0 & remove from the list as well.
# So if input is ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who'] then 'All' will be 
# printed which is positioned at 0'th position & thereafter 'All' won't be part of the list.
	print (word)
	
def print_last_word(words):
	"""Print the last word after popping it off."""
	word = words.pop(-1) # pop will pick the last word in the given input & deletes it. -1 stands for last word.
#So, for same above inputs, it will print 'who'
	print(word)
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last word of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)