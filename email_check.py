x = eval(input('How many email addreeses you are going to entered? '))
stud = 0
prof = 0
inc = 0
for i in range(x):
	y = input('Enter the email address: ')
	for i in y:
		if i == '@':
			s = y.index(i)
			s_new = y[(s+1):]
			print(s_new, 's_new')
			if s_new == 'student.college.edu.':
				stud = stud + 1
				print(stud)
			elif s_new == 'prof.college.edu.':
				prof = prof + 1
			else:
				print ('This is neither student nor prof email ids & will be ignored...')
				inc = inc + 1

if stud != 0 and prof != 0:
	print ('Entered email addresses contains both student & professors email ids.')
elif stud !=0 and prof == 0:
	print ('Entered email ids are of only students.')
elif stud == 0 and prof != 0:
	print ('Entered email ids are of only professors.')
else:
	print ('You have neither entered students nor entered professors email ids.')

