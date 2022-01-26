#from sys import argv

#script, a, b = argv

#a = float(argv[1])
#b = float(argv[2])



def add(a, b):
	print ( "Addition of %s + %s: " % (a, b), end = '' )
	return a + b
	
def sub(a, b):
	print ( "Subtraction of %s - %s: " % (a, b), end = '')
	return a - b
	
def mult(a, b):
	print ("Multiplication of %s * %s: " % (a, b), end = '')
	return a * b
	
def divide(a, b):
	print ("Division of %s / %s: " % (a, b), end = '')
	return a / b
	
#print ("Please type RETURN/ENTER to start with the calculation.")
#input()

#x = input('>')

#print (x)

#print ("Please provide the operations like +, -, *, /")

#y = input(prompt)

#print ("We are running 4 arithmatic operations using %s script" % script)
#print (add(a, b))
#print (sub(a, b))
#print (mult(a, b))
#print (divide(a, b))

x = float(input("Please provide first number: "))
operator = input("Please enter operation to be performed i.e. +, -, *, / :  ")
y = float(input("Please provide second number: "))

if operator == "+":
	print (add(x, y))
	
elif operator == "-":
	print (sub(x, y))
	
elif operator == "*":
	print (mult(x, y))
	
elif operator == "/":
	print (divide(x, y))
	
else:
	print ("Please provide valid operator from given lists.")
	

