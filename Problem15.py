#Simple combinatorics problem, generalized for any rectanglular graph
def factorial(x):
	ndx = 1
	temp = x
	while ndx < x:
		temp *= ndx
		ndx += 1
	return temp


horizontal = input("Horizontal: ")
vertical = input("Vertical: ")
horizontal = int(horizontal)
vertical = int(vertical)

answer = factorial(horizontal + vertical) / (factorial(horizontal) * factorial(vertical))
print(answer)
