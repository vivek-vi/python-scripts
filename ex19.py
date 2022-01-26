def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print ("You have %d cheeses!" % cheese_count)
	print ("You have %d boxes of crackers!" % boxes_of_crackers)
	print ("Man that's enough for party!")
	print ("Get a blanket.\n")
	
print ("We can just give the function numbers directly as follows")
cheese_and_crackers(20, 30)

print ("Or we can use variables instead of putting numbers as follows")

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print ("We can even do maths inside too:")

cheese_and_crackers(10 + 20, 5 + 6)

print ("We can even combine both variable & maths provided both are integer as follows")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def square(x):
	print ("Square of the given number is %s" % (x * x))
	

y = int(input("Please provide your lucky number & we will provide square of it: "))
square(y)

# Below is the code optimization

square(int(input("Please provide another your lucky number & we will provide square of it: ")))