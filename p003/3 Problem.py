import math

number = 600851475143
highest_prime = 0
number_root = math.sqrt(number)
for i in range (3, int(number_root)+1, 2):
	if number % i == 0:
		flag = 0
		if i % 2 == 0:
			if i != 2:
				flag = 1
		for j in range(3, i, 2):
			#print(i, j)
			if i % j == 0:
				flag = 1
				break
		if flag == 0:
			highest_prime = i
print("Highest prime is -", highest_prime)
	
		