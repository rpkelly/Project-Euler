nums = []

x = 0
while x < 2000000:
	nums.append(True)
	x += 1
nums[0] = False
nums[1] = False

i = 2
while i < 1000000:
	if nums[i] == True:
		j = 2
		while i * j < 2000000:
			nums[i*j] = False
			j += 1
	i += 1

sop = 0
ndx = 0
while ndx < 2000000:
	if nums[ndx] == True:
		sop += ndx
	ndx += 1
print(sop)
