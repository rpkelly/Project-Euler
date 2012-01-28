# c = 1000 - a - b
# a^2 + b^2 = (1000 - a - b)(1000 - a - b)
# a^2 + b^2 = 1000000 - 1000a - 1000b - 1000a + a^2 + ab - 1000b +ab + b^2
# 0 = 500000 - 1000a - 1000b + ab
# 1000b - ab = 500000 - 1000a
# b(1000 - a) = 500000 - 1000a
# b = (500000 - 1000a)/(1000 - a)

#a + b + c = 1000
#a^2 + b^2 = c^2

#Increment while a < 333 starting at a = 100
a = 100
while a < 333:
	b = (500000 - (1000 * a))/(1000 - a)
	c = 1000 - a - b
	b = int(b)
	c = int(c)
	if c**2 == a**2 + b**2:
		print(a, b, c)
		break
	a += 1
print(a * b * c)
