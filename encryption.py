x = input('Enter a string & will encrypt it: ')

y = ''
z = ''
for i in range(len(x)):
	if i % 2 == 0:
		y = y + x[i]
for j in range(len(x)):
	if j % 2 == 1:
		z = z + x[j]

a = y + z

print ('Encrypted string is: ', a)

#decryption algo
orig = ''
l = len(a)
#print(type(l), l//2)
if l % 2 == 0:
	even_char = a[:(l // 2)]
	print ('even_char', even_char)
	odd_char = a[(l // 2):]
	print ('odd_char', odd_char)
	for n in range(len(a)):
		if n < len(odd_char):
#			print(n, 'n')
			orig = orig + even_char[n] + odd_char[n]
		elif n <= (len(even_char)-1):
#			print(n, 'else n')
			orig = orig + even_char[n]
else:
	even_char = a[:((l // 2)+1)]
	print ('even_char', even_char)
	odd_char = a[((l // 2)+1):]
	print ('odd_char', odd_char)
	for n in range(len(a)):
		if n < len(odd_char):
#			print(n, 'n')
			orig = orig + even_char[n] + odd_char[n]
		elif n <= (len(even_char)-1):
#			print(n, 'else n')
			orig = orig + even_char[n]
	

print ('Original word is: ', orig)