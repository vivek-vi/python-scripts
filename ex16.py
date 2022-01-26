from sys import argv

script, filename = argv

print ("We are going to erase %r." % filename)
print ("If you don't want that then hit CTRL+c")
print ("If you do want then hit RETURN/ENTER")

input("?")

print ("Opening the file...")
target = open(filename, 'w') # 'w' stands as 'write' mode.

# Below truncate function is not necessary & by default 'w' mode overwrites existing file content.
# print ("Truncating the file, Goodbye...")
# target.truncate()

print ("Now I going to ask you about 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these into file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#We can replace above 6 write statements by below single write function with placeholders using format
# function

target.write('{0}\n{1}\n{2}\n'.format(line1, line2, line3))

print ("And finally we close it.")
target.close()
