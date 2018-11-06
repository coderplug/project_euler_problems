def largest_product_sep(num_digits):
	file_numbers = open('number.txt')
	s_number = ''
	max = 0
	for x in file_numbers:
		s_number = x.strip()
		length = len(s_number)
		for i in range(0, length-num_digits+1):
			result = 1;
			s_combo = s_number[i:i+num_digits]
			if '0' in s_combo:
				continue
			for j in s_combo:
				result *= int(j)
			print(s_combo, result);
			if result > max:
				max = result
	return max
	
def largest_product(num_digits):
	file_numbers = open('number.txt')
	s_number = ''
	max = 0
	for x in file_numbers:
		s_number += x.strip()
	length = len(s_number)
	for i in range(0, length-num_digits+1):
		result = 1;
		s_combo = s_number[i:i+num_digits]
		if '0' in s_combo:
			continue
		for j in s_combo:
			result *= int(j)
		print(s_combo, result);
		if result > max:
			max = result
	return max
print(largest_product(13))