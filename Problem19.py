months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1901
day = 2
count = 0
ndx = 0

while year < 2001:
	day += months[ndx % 12]
	if ndx % 12 == 1:
		if year % 4 == 0:
			day += 1
	day = day % 7
	if day == 0:
		count += 1
	ndx += 1
	if ndx % 12 == 0:
		year += 1
print(count)
