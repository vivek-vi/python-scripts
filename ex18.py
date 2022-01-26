# This one is like our scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print ("arg1: %r, arg2: %r" % (arg1, arg2))
	
# Ok, *args is pointless so we can just do this
def print_two_again(arg1, arg2):
	print ("arg1: %r, arg2: %r" % (arg1, arg2))
	
# This just take 1 argument
def print_one(arg1):
	print ("arg1: %r" % arg1)
	
# This one takes no argument
def print_none():
	print ("I got nothing")
	
x = input("What is your name? ")
y = input ("What is your surname? ")

print_two(x, y)   # Made it dynamic with user input
print_two_again("Vivek", "Vidhate")
print_one("Cool!")
print_none()
