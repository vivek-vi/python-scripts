tabby_cat = "\tI'm tabbed in."    # \t shift the cursor 1 tab position.
persian_cat = "I'm split\non a line." #\n shift the cursor on new line.
backslash_cat = "I'm \\ a \\ cat." # Double backslash is to escape actual backslash character in string so
# it will print backslash used in string. Overhere we escaped backslash but using same logic we can
# escape Single quote, double quote etc. present in the string itself. 

fat_cat = """I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass """

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
