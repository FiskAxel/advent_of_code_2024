with open('input01.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	list1, list2 = [], []
	for line in input:
		a = line.split('   ')
		list1.append(int(a[0]))
		list2.append(int(a[1]))
	list1.sort()
	list2.sort()

	tot = 0
	for i in range(len(list1)):
		tot += abs(list1[i] - list2[i])

	print(f"Part 1: {tot}")

	# PART 2
	dict = {}
	for e in list1:
		dict[e] = 0

	for e in list2:
		if e in dict:
			dict[e] += 1
	
	sum = 0
	for e in dict:
		sum += int(e) * dict[e]
	print(f"Part 2: {sum}")
