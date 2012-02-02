f = open("prob13.txt", 'r')
ndx = 0
sums = 0
while ndx < 100:
	s = f.readline()
	num = int(s)
	sums += num
	ndx += 1
numstring = str(sums)
ndx = 0
while ndx < 10:
	print(numstring[ndx], end='')
	ndx += 1
print('')
