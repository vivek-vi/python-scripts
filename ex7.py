print ("Mary had a little lamb")
print ("It's fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
print ( "." * 10) # this will print dot[.] notation 10 times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that 'end' argument in below print statement & check the behavior on removing it.
print ( end1 + end2 + end3 + end4 + end5 + end6, end = ' and ')
print ( end7 + end8 + end9 + end10 + end11 + end12)

# Print in python by default executed on new line so if we want to print 2 different print statement over 
# single line then use argument 'end' by assigning whitespace character string Or comma as required
# separator