def add(a, b):
	print ("Adding %d + %d" %(a, b))
	return a + b # return keyword assigns the result to the called variable, in this case 'age'
	
def subtract(a, b):
	print ("Subtracting %d - %d" % (a, b))
	return a - b
	
def multiply(a, b):
	print ("Multiplying %d * %d" % (a, b))
	return a * b
	
def divide(a, b):
	print("Dividing %d / %d" % (a, b))
	return a / b
	
print ("Let's do some maths with just functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(20, 4)
iq = divide(260, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for extra credit, type it in anyway
print ("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")

# My own logic

new_1 = divide(iq, subtract(weight, add(height, multiply(age, 3))))

print ("Some different operations: ", new_1)

# Let's take inputs from the user.

x = int(input("Please enter quantity of items: "))
y = float(input("Please enter item price: "))
z = multiply(x, y)

print ("You have spent %s Rs. for this purchase" % z)