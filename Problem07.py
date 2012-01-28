#Given 6 primes; up to 13
primes = 6
testval = 15
while primes < 10001:
	if testval%6 != 1 or testval%6 !=5:
		ndx = 2
		while ndx <= testval ** 0.5:
			if testval % ndx == 0:
				prime = False
				break
			else:
				prime = True
			ndx += 1
		if prime == True:
			primes += 1
	testval += 2

print (testval - 2)
