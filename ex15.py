from sys import argv

script, filename = argv

txt = open(filename) # File should be open before performing RU operations.

print ("Here's your file %s:" % filename)
print (txt.read())

print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())