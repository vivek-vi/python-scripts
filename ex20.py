from sys import argv

script, input_file = argv

def print_all(f):
	print (f.read())
	
def rewind(f):
	print (f.seek(0))  # Seek function will move the cursor & in this case, it sets to the file beginning.
	
def print_a_line(line_count, f):
	print (line_count, f.readline()) 

# readline() function returns Single line content with newline & cursor go to the next line in a file.
# If file is close & re-open then each time it will start from first line but if it's not then 
# it will print next subsequent lines 

current_file = open(input_file)

print ("First lets print the whole file:\n")

print_all(current_file)

print ("Now let's rewind like a tape")

rewind(current_file)

print ("Let's print 3 lines: ")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

