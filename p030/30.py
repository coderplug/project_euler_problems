def get_digits(n):
	digits = [];
	while n:
		digits = [n % 10] + digits;
		n = n // 10;
	return digits;
total = 0;
for number in range(2, 1000000):
	digits = get_digits(number);
	sum = 0;
	#print(number, digits);
	for digit in digits:
		sum += digit**5;
	if sum == number:
		print(number);
		total += number;
print(total);
	