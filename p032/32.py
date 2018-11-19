def get_digits(n):
	digits = [];
	while n:
		digits = [n % 10] + digits;
		n = n // 10;
	return digits;
def check_number_2(a, b):
	digits_a = get_digits(a);
	digits_b = get_digits(b);
	digits_prod = get_digits(a*b);
	combined_digits_s = (set(digits_a).union(set(digits_b))).union(digits_prod);
	combined_digits_l = digits_a + digits_b + digits_prod;
	if len(combined_digits_s) == len(combined_digits_l) and \
		len(combined_digits_s) == 9 and 0 not in combined_digits_l:
		return True, combined_digits_l;
	return False, combined_digits_l;
		
def check_number(taken_numbers, n):
	digits = get_digits(n);
	combined_numbers = list(set(taken_numbers).union(set(digits)));
	if digits == list(set(digits)):
		return False, combined_numbers;
	elif 0 in combined_numbers:
		return False, combined_numbers;
	elif len(taken_numbers) + len(digits) > 9:
		return False, combined_numbers;
	elif len(combined_numbers) != len(taken_numbers) + len(digits):
		return False, combined_numbers;
	return True, combined_numbers;
products = set()
for a in range(1, 10000):
	for b in range(1, 10000):
		if len(str(a) + str(b)) > 5:
			break;
		is_valid, taken = check_number_2(a, b);
		if is_valid is True:
			products.add(a*b);
			print(a, b, a*b, taken);
		'''is_valid, taken = check_number([], a);
		if is_valid is True:
			is_valid, taken = check_number(taken, b);
			if is_valid is True:
				is_valid, taken = check_number(taken, a*b);
				if is_valid is True and len(taken) == 9:
					products.add(a*b);
					#print(a, b, a*b, taken);
		'''
print(sum(products));