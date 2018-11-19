#import math
def is_triangular(value):
	position = ((8*value+1)**(1/2)-1)/2;
	if position == int(position):
		return True;
	return False;
def is_pentagonal(value):
	position = ((24*value+1)**(1/2)+1)/6;
	if position == int(position):
		return True;
	return False;
def is_hexagonal(value):
	position = ((8*value+1)**(1/2)+1)/4;
	if position == int(position):
		return True;
	return False;
def generate_pentagonal(p_from, p_to):
	pentagonal_numbers = [];
	for i in range(p_from, p_to+1):
		pentagonal_numbers += [int((1/2)*i*(3*i-1))];
	return pentagonal_numbers;
for pentagonal in generate_pentagonal(1, 1000000):
	if is_triangular(pentagonal) is True and is_hexagonal(pentagonal) is True:
		print(pentagonal);