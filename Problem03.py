import cmath

x = 600851475143
n = 2
a = x
m = 0
root = x**0.5

while n < (root):
	if a % n == 0:
		a = a / n
		if n > m:
			m = n
		n = 1
	n += 1
print(m)
