import math
amicable_numbers = []
for a in range(2, 10000):
	sum_a = 1
	for j in range(2, int(math.sqrt(a) + 1)):
		if a % j == 0:
			sum_a += j
			sum_a += a//j
	if int(math.sqrt(a))**2 == a:
		sum_a -= int(math.sqrt(a))		
	if a != sum_a:
		sum_b = 1
		for j in range(2, int(math.sqrt(sum_a) + 1)):
			if sum_a % j == 0:
				sum_b += j
				sum_b += sum_a//j
		if int(math.sqrt(sum_a))**2 == sum_a:
			sum_b -= int(math.sqrt(sum_a))
		print(a, sum_a, sum_b)
		if a == sum_b and sum_a not in amicable_numbers:
			amicable_numbers.append(sum_a)
			amicable_numbers.append(a)
print(sum(amicable_numbers))