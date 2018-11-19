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
def check_palindrome(dig_list):
	list_length = len(dig_list);
	for i in range(math.ceil(list_length)):
		if(dig_list[i] != dig_list[list_length-(i+1)]):
			return False;
	return True;
palindrome_dict = {};
for i in range(1000000):
	if check_palindrome(get_digits(i)) is True:
		palindrome_dict[i] = int("{0:b}".format(i));
#print(palindrome_dict);
result = []
for key, value in palindrome_dict.items():
	if check_palindrome(get_digits(value)) is True:
		result += [key];
print(result)
print(len(result));
print(sum(result));