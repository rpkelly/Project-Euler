def finder():
	x = 999
	y = 999
	while True:
		z = x * y
		n = str(z)
		if n[0] == n[len(n)-1]:
			if n[1] == n[len(n)-2]:
				if n[2] == n[len(n)-3]:
					return( z )
		if x - y > 100:
			x -= 1
			y = x
		else:
			y -= 1

print(finder())
