#Same as Problem18.py only opens 'triangle.txt' instead of prob18.txt

import re
lists = []
f = open("triangle.txt", 'r')
#For loop reads in triangle of arbitrary size
for line in f:
	lists.append(re.split('\D+', line))

ndx = 0
while ndx < len(lists):
	lists[ndx].remove('')
	ndx += 1

ndx = len(lists) - 2

while ndx > -1:
	mdx = 0
	while mdx < len(lists[ndx]):
		if int(lists[ndx+1][mdx]) > int(lists[ndx+1][mdx+1]):
			lists[ndx][mdx] = int(lists[ndx][mdx]) + int(lists[ndx+1][mdx])
		else:
			lists[ndx][mdx] = int(lists[ndx][mdx]) + int(lists[ndx+1][mdx+1])
		mdx += 1
	ndx -= 1
print(lists[0][0])
