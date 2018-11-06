import math

def get_prime():
	position = int(input())
	counter = 1
	number = 1
	if position == 1:
		return 2
	else:
		while counter != position:
			number += 2
			flag = False
			if number % 2 == 0:
				flag = True
			else:
				for x in range (3, int(math.sqrt(number))+1, 2):
					if number % x == 0:
						flag = True
						break
			if flag == False:
				counter += 1
		return number
print(get_prime())