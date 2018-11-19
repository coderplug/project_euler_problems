import sys
from decimal import Decimal as D
from fractions import Fraction
def get_digits(n):
	digits = [];
	while n:
		digits = [n % 10] + digits;
		n = n // 10;
	return digits;
	
def check_curious(a, b):
	digits_a = get_digits(a);
	digits_b = get_digits(b);
	if a/b >= 1:
		return False;
	if digits_a[0] == digits_b[1]:
		if digits_b[0] != 0 and (a / b) == (digits_a[1] / digits_b[0]):
			return True;
	elif digits_a[1] == digits_b[0]:
		if digits_b[1] != 0 and (a / b) == (digits_a[0] / digits_b[1]):
			return True;
	return False;
denominators = [];
max_value = D(1);
for a in range(10, 100):
	for b in range(10, 100):
		if check_curious(a, b) is True:
			denominators += [b];
			max_value *= D(a)/D(b);
			print(max_value);
			print(a, " / ", b);
fract = Fraction(max_value);
print(fract.denominator);
'''
max_value = max(denominators);	
for i in range(2, sys.maxsize**10):
	is_valid = True;
	common_denom = max_value*i;
	for j in denominators:
		#print(j);
		if common_denom%j!=0:
			is_valid = False;
			break;
	if is_valid is True:
		print(common_denom);
		break;
'''	