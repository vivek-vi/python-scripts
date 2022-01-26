x = input('Enter your name: ')
data = """ 
Dear zebra_full,
I am pleased to offer you our new Platinum Plus Rewards
card at a special introductory APR of 47.99%.  zebra,
an offer like this does not come along every day, so I
urge you to call now toll-free at 1-800-314-1592. We
cannot offer such a low rate for long, zebra, so call
right away."""

data = data.replace('zebra_full', x)

first_name = ''

for i in range(len(x)):
	if x[i] == ' ':
		pos = x.index(' ')
		first_name = first_name + x[:pos]

data = data.replace('zebra', first_name)

print (data)
