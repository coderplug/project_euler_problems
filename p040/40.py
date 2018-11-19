import math
def get_digit_from_fraction(position, digit_sum):
	index = 0;
	pos = position;
	for sum in digit_sum:
		if sum > pos:
			#print(pos);
			index = digit_sum.index(sum);
			power_number = int(math.ceil(pos/(index+1))-1); #45
			number = 10**index + power_number; #45.5-1 -> 45
			digit = pos - power_number * (index+1); #45.5, 91 - 0, 46, 92 -1
			print(number, str(number)[digit-1]);
			return int(str(number)[digit-1]);
		else:
			pos -= sum;
	print(">",index);
digit_sum = [];
for i in range(6):
	digit_sum += [(i+1)*(10**(i+1)-10**i)];
print(digit_sum);
product = get_digit_from_fraction(10**0, digit_sum) * \
	get_digit_from_fraction(10**1, digit_sum) * \
	get_digit_from_fraction(10**2, digit_sum) * \
	get_digit_from_fraction(10**3, digit_sum) * \
	get_digit_from_fraction(10**4, digit_sum) * \
	get_digit_from_fraction(10**5, digit_sum) * \
	get_digit_from_fraction(10**6, digit_sum);
print(product);
#fraction = "";
#for j in range(1, 100):
#	fraction += str(j);
#print(fraction[99]);