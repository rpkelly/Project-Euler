#Find the sum of all primes less than 2,000,000

#Use the Sieve of Erastosthenes to find all primes

primes = []
x = 2
#Create a list of all numbers from 2 to 2,000,000
while x < 2000001:
	primes.append(x)
	x += 1

ndx = 0
while ndx < len(primes):
	mdx = ndx
	while mdx < len(primes):	
		if primes[mdx] % primes[ndx] == 0 and primes[mdx] != primes[ndx]:
			primes.remove(primes[mdx])
			mdx -= 1
		mdx += 1
	ndx += 1

sop = 0
for i in primes:
	sop += i
print(sop)
