with open('input01.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	list1, list2 = [], []
	for line in input:
		a = line.split('   ')
		list1.append(int(a[0]))
		list2.append(int(a[1]))
	
	# PART 1
	list1.sort()
	list2.sort()
	dif = sum([abs(a - b) for a, b in zip(list1, list2)])
	print(f'Part 1: {dif}')

	# PART 2
	occurances = {e: list2.count(e) for e in list1}
	similarityScore = sum(e * count for e, count in occurances.items())
	print(f'Part 2: {similarityScore}')
