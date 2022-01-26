from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s." % (from_file, to_file))

# We could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()

# We can define 'indata' with open & r mode.
# But it's just pointer & not have content of the file so we have to use read() function
# during copying it's content as well as counting the length.

indata = open(from_file, 'r') # 'r' stands for 'read' mode which is default.

print ("The input file is %d bytes long" % len(indata.read()))

print ("Does the output file exists? %r" % exists(to_file))
print ("Ready, hit RETURN/ENTER to continue, CTRL+c to abort.")
input() # This is to take empty input when user press enter.

out_file = open(to_file, 'w')
out_file.write(indata.read())

print ("Alright, all done!")

out_file.close()
#in_file.close()