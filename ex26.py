def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#def print_first_word(words) # Function has syntax error with missing colon
def print_first_word(words):
    """Prints the first word after popping it off."""
#    word = words.poop(0)  #Spelling mistake for 'pop' function.
    word = words.pop(0)
    print (word)  # Added parenthesis because I'm running in python3

def print_last_word(words):
    """Prints the last word after popping it off."""
#    word = words.pop(-1   # Closing parenthesis is missing for 'pop' function.
    word = words.pop(-1)
    print (word)    # Added parenthesis because I'm running in python3

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print ("Let's practice everything.") # Added parenthesis because I'm running in python3
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') # Added parenthesis because I'm running in python3

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation (Updated spelling of explanation)
\n\t\twhere there is none.
"""


print ("--------------") # Added parenthesis because I'm running in python3
print (poem) # Added parenthesis because I'm running in python3
print ("--------------") # Added parenthesis because I'm running in python3

#five = 10 - 2 + 3 - 5 # Incorrect maths.
five = 10 - 2 + 3 - 6
print ("This should be five: %s" % five) # Added parenthesis because I'm running in python3

def secret_formula(started):
    jelly_beans = started * 500
#    jars = jelly_beans \ 1000  # Incorrect operator
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# beans, jars, crates == secret_formula(start-point) #Incorrect variable passed i.e. start-point &
# incorrect operator used.
beans, jars, crates = secret_formula(start_point)

print ("With a starting point of: %d" % start_point) # Added parenthesis because I'm running in python3
#print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates) it should be beans instead of jeans.
print ("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print ("We can also do that this way:") # Added parenthesis because I'm running in python3
#print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont
#Above line has incomplete parenthesis as well as spelling mistake for crates.
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))

sentence = "All god\tthings come to those who weight."

#words = ex25.break_words(sentence) # Incorrect function call with ex25
words = break_words(sentence)
#sorted_words = ex25.sort_words(words) # Incorrect function call with ex25
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
#.print_first_word(sorted_words) # Incorrectly called with dot notation.
print_first_word(sorted_words)
print_last_word(sorted_words)
#sorted_words = ex25.sort_sentence(sentence) # Incorrect function call with ex25

sorted_words = sort_sentence(sentence)
#prin sorted_words incorrect function call with prin
print (sorted_words)

#print_irst_and_last(sentence) # Again incorrect function name 'irst' instead of 'first'
print_first_and_last(sentence)

#   print_first_a_last_sorted(senence) # Incorrect indentation, incorrect function name & incorrect 
# passed variable as "senence"

print_first_and_last_sorted(sentence)
