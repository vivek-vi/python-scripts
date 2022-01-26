#A list consisting of the integers 0 through 49

x = []

for i in range(0,50):
	x = x + [i]

print(x)

#A list containing the squares of the integers 1 through 50

y = []

for i in range(1,51):
	y = y + [i ** 2]
	
print(y)

#The list ['a', 'bb', 'ccc', 'dddd', … ] that ends with 26 copies of the letter z

z = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p = []
for i in range(0,26):
	p = p + [z[i] * (i+1)]

print(p)
