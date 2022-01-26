from random import randint
x = input('Enter your password: ')
x = x.lower()
enc = ''
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in x:
	#print(x[i], 'x-i')
	pos = char.index(i)
	jump = randint(1,26)
	y = pos + jump
	if y < 25:
		i = char[y]
		enc = enc + i
	else:
		y = y - 26
		i = char[y]
		enc = enc + i

print(enc) 

#decryption

for j in enc:
	