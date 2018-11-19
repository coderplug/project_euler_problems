def get_number(dig_list):
	index = 0;
	number = 0;
	for digit in dig_list:
		index+=1;
		number += digit*10**(len(dig_list)-index);
	return number;
def property_validity(index, current_digits):
	if index == 0:
		return True;	
	elif index == 1:
		return True;
	elif index == 2:
		return True;
	elif index == 3 and current_digits[index]%2 == 0:
		return True;
	elif index == 4 and (current_digits[index-2] + current_digits[index-1] + current_digits[index])%3 == 0:
		return True;
	elif index == 5 and current_digits[index]%5 == 0:
		return True;
	elif index == 6 and (get_number([current_digits[index-2], current_digits[index-1], current_digits[index]]))%7 == 0:
		return True;
	elif index == 7 and (get_number([current_digits[index-2], current_digits[index-1], current_digits[index]]))%11 == 0:
		return True;
	elif index == 8 and (get_number([current_digits[index-2], current_digits[index-1], current_digits[index]]))%13 == 0:
		return True;
	elif index == 9 and (get_number([current_digits[index-2], current_digits[index-1], current_digits[index]]))%17 == 0:
		return True;
	else:
		return False;
def generate_pandigitals(current_digits, numbers, index):
	next_numbers = list(numbers);
	numbers.sort(reverse=True);
	sum = 0;
	for number in numbers:
		if property_validity(index, current_digits + [number]) is False:
			continue;
		#print(current_digits + [number]);
		if index == 0 and 0 not in next_numbers:
			next_numbers += [0];
		if index != 9:
			next_numbers.remove(number);
			sum += generate_pandigitals(current_digits + [number], next_numbers, index+1);
			next_numbers += [number];
		else:
			digits = current_digits + [number];
			final_number = get_number(digits);
			sum += final_number;
			print(final_number);
	return sum;
available = [9, 8, 7, 6, 5, 4, 3, 2, 1];
total = generate_pandigitals([], available, 0);
print(total);