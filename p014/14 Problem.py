maximum = 0
dictionary = {}
for i in range(1, 1000000):
	steps = 0
	number = i
	while number != 1:
		if number in dictionary:
			steps += dictionary[number]
			break;
		steps += 1
		if number % 2 == 0:
			number /= 2
		else:
			number = 3 * number + 1
	dictionary[i] = steps
	if maximum < steps:
		max_num = i
		maximum = steps
print(maximum, max_num)