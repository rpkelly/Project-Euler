def factorial(x):
	ndx = 1
	ans = x
	while ndx < x:
		ans *= ndx
		ndx += 1
	return ans

print(sum(map(int,str(factorial(100)))))
