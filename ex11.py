print ("How old are you?", end = ' ')
age = input()    # input() is builtin function to get data from user.
print ("How tall are you?", end = ' ')
height = input()
print ("How much do you weigh", end = ' ')
weight = input()

print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))