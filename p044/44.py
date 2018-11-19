import math
def is_pentagonal(value):
	n = ((24*value+1)**(1/2)+1)/6
	if n == int(n):
		return True;
	return False;
def diff(first, second):
	second = set(second);
	return [item for item in first if item not in second];
def test_property(p1, p2, pentagonal_list):
	#print(p1, p2, p1+p2, "->", int(math.fabs(p1-p2)));
	if is_pentagonal(p1+p2) is True and is_pentagonal(p1-p2) is True:
		return True, int(math.fabs(p1-p2));
	else:
		return False, None;
def generate_pentagonal(p_from, p_to):
	pentagonal_numbers = [];
	for i in range(p_from, p_to+1):
		pentagonal_numbers += [int((1/2)*i*(3*i-1))];
	return pentagonal_numbers;
pentagonal_list = generate_pentagonal(1, 100000);
#print(pentagonal_list);
for first_index in range(100000):
	for second_index in range(first_index-1, -1, -1):
		first_number = pentagonal_list[first_index];
		second_number = pentagonal_list[second_index];
		valid, d_value = test_property(first_number, second_number, pentagonal_list);
		if valid is True:
			print(d_value);
			exit();
'''
	#print(first_number);
	for second_number in diff(pentagonal_list, [first_number]):
		#print(second_number);
		valid, d_value = test_property(first_number, second_number, pentagonal_list);
		if valid is True:
			print(d_value);
			'''