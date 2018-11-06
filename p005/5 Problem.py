import math
def smallest_multiple(limit):
	sum = 1
	for i in range(2, limit):
		flag = 0
		if i % 2 == 0:
			if i != 2:
				flag = 1
		else:
			for j in range (2, int(math.sqrt(i))+1):
				if i%j == 0:
					flag = 1
					break
		if flag == 0:
			number = limit
			index = 0
			while number > i:
				index += 1
				number /= i
			sum *= i**index
	return sum
print(smallest_multiple(20))