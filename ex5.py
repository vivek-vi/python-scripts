my_name = "Vivek Vidhate"
my_age = 32
my_height = 177
my_weight = 76.7
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

# %s is a placeholder for string values & variable should be defined post % operator
# %s uses string conversion via str() before formatting.
# So it can accept numeric values & automatically does the type conversion that means
# we can still use %s instead of %d in below where it doesn't perform decimal conversion &
# retains flot number whatever is defined. 

print ("Let's talk about %s." % my_name)

# %d is a placeholder for numeric values & variable should be defined post % operator.
# %d uses decimal conversion via int() before formatting that means float is not supported &
# rounded off to the integer so if we define weight as 76.6 then it would be 76
# %d can't accept non numeric values & thrown type error.

print ("He's %d centimeter tall." % my_height)
print ("He's %d kilogram heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

print ("If I add %d, %d, and %d I get %d." % ( \
my_age, my_height, my_weight, my_age + my_height + my_weight))

