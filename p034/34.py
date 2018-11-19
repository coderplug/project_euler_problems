import math
def get_number(dig_list):
	index = 0;
	number = 0;
	for digit in dig_list:
		index+=1;
		number += digit*10**(len(dig_list)-index);
	return number;
def get_digits(n):
	digits = [];
	while n:
		digits = [n % 10] + digits;
		n = n // 10;
	return digits;
result = 0;
for a in range(0, 10):
	for b in range(0, 10):
		for c in range(0, 10):
			for d in range(0, 10):
				for e in range(0, 10):
					for f in range(0, 10):
						for g in range(0, 10):
							factorials = [a, b, c, d, e, f, g];
							index = 0;
							for factorial in factorials:
								if factorial != 0:
									break;
								index+=1;
							factorials = factorials[index:];
							sum = 0;
							for fact in factorials:
								sum += math.factorial(fact);
							if sum <= 2:
								continue;
							d_sum = get_digits(sum);
							#print(factorials, d_sum);
							#while len(d_sum) < 7:
							#	d_sum = [0] + d_sum;
							#print(factorials, d_sum);
							if len([i for i, j in zip(factorials, d_sum) if i == j]) == len(factorials):
								print(factorials, d_sum, get_number(d_sum));
								result += get_number(d_sum);
print(result);