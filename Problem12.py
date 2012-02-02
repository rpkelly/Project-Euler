factors = 0
num = 2
trinum = 3

while factors < 500:
	ndx = 2
	exponents = []
	mdx = 0
	lastndx = 0
	location = 0
	num += 1
	trinum += num
	tempnum = trinum
	
	root = trinum ** 0.5
	while ndx < root:
		if tempnum % ndx == 0:
			tempnum = tempnum/ndx
			if ndx == lastndx:
				exponents[location] += 1
				lastndx = ndx
			else:
				exponents.append(2)
				location = len(exponents) - 1
				lastndx = ndx
			ndx -= 1
		ndx += 1
	factors = 1
	while mdx < len(exponents):
		if len(exponents) == 0:
			break
		factors *= exponents[mdx]
		mdx += 1
print(trinum)
print(exponents)
