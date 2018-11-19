def iterate(current_digits, numbers, index):
	next_numbers = list(numbers);
	numbers.sort(reverse=True);
	for number in numbers:
		if index != 8:
			if number == 0:
				next_numbers.remove(9-index);
				iterate(current_digits + [number], next_numbers, index+1);
				next_numbers += [9-index];
			else:
				tmp = False;
				#print(next_numbers, number, index);
				if 0 in next_numbers:
					tmp = True;
					next_numbers.remove(0);
				next_numbers.remove(number);
				iterate(current_digits + [number], next_numbers, index+1);
				if tmp is True:
					next_numbers += [0];
				next_numbers += [number];
		else:
			digits = current_digits + [number];
			final_number = get_number(digits);
			#print(final_number);
			if number != 0 and number%2 != 0 and isprime(final_number) is True:
				print(final_number);
def get_number(dig_list):
	index = 0;
	number = 0;
	for digit in dig_list:
		index+=1;
		number += digit*10**(len(dig_list)-index);
	return number;
def isprime(n):
    """Returns True if n is prime."""
    if n < 2:
        return False;
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
available = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0];
iterate([], available, 0);