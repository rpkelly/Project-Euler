#Create a dictionary for each value, only go until you've found something
#in the dictionary, then stop

num = 999999
numList = []
ndx = 0
while ndx < 1000000:
	numList.append(0)
	ndx += 1

while num > 1:
	val = num
	hailstones = 1
#Only need to go to 500,000 as there will be a sister for each one below
	while val > 500000:
		if val < 1000000:
			if numList[val] != 0:
				hailstones += numList[val]
				break
		if val % 2 == 0:
			val = val//2
		else:
			val = 3 * val + 1
		hailstones += 1
	numList[num] = hailstones
#	print(num, numList[num])
#Only need to check odd numbers, each even could be bigger by 2n
	num -= 2
print(numList.index(max(numList)))
