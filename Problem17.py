upToFifteen = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
twentToNinet = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
num = 1
sums = 0
while num < 1000:
	last = sums
	hundreds = num // 100
	tens = num // 10 - (10 * hundreds)
	ones = num - (10 * tens) - (100 * hundreds)
	if ones + (tens * 10) < 20:
		sums += upToFifteen[num - (hundreds * 100)]
	else:
		sums += upToFifteen[ones] + twentToNinet[tens]
	if hundreds:
		sums += 7 + upToFifteen[hundreds]
		if num % 100 != 0:
			sums += 3
	print("Num:", num, "Sum:", sums, "Diff:", sums - last, sep=' ')
	num += 1
sums += 11
print(sums)
