def highest_path(level, numbers):
	for i in range(0, level):
		if numbers[level][i] > numbers[level][i+1]:
			numbers[level-1][i] += numbers[level][i]
		else:
			numbers[level-1][i] += numbers[level][i+1]
	if level - 1 == 0:
		return numbers[0][0]
	else:
		return highest_path(level - 1, numbers)
	
file = open("triangle.txt")
numbers = file.readlines()
numbers = [i.rstrip().split() for i in numbers]
numbers = [[int(j) for j in i] for i in numbers]
print(highest_path(len(numbers)-1, numbers))
"""
i, x[i] = 1, 2         # i is updated, then x[i] is updated
"""