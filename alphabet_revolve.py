alpha = 'abcdefghijklmnopqrstuvwxyz'
new = ''
for i in range(26):
	new = alpha[i:] + alpha[:(i)]
	print (new)