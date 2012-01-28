x = 5
y = 0
z = 0
while (x * y) < 1000:
	z = z + (x * y)
	y = y + 1
x = 3
y = 0
while (x * y) < 1000:
	if (x * y) % 5 != 0:
		z = z + (x * y)
	y = y + 1
print (z)
