a, b = 0, 1
x = 0
while x < 4000000:
	a, b = b, a+b
	if b % 2 == 0:
		x = x + b
print (x)
