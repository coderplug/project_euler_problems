import collections
max = 0;
max_number = 0;
for i in range(1, 10000):
	maximum_products = int(9/len(str(i)));
	pandigital = "";
	for j in range(1, maximum_products+1):
		number = i*j;
		pandigital += str(number);
		if len(pandigital) == 9:
			break;
	if len(pandigital) == 9:
		valid_pandigital = True;
		for key, value in collections.Counter(pandigital).items():
			#print(key, value);
			if key == "0" or value > 1:
				valid_pandigital = False;
				break;
		if valid_pandigital is True:
			print(pandigital);
			if max < int(pandigital):
				max = int(pandigital);
				max_number = i;
print(max, max_number);