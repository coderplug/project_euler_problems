import sys

def count_period(denom):
	for i in range(2, sys.maxsize**10):
		ten_pow_min_1 = 10**i-1;
		if ten_pow_min_1 % denom == 0:
			return i;
max_period = 0;
max_index = 0;
for i in range(2, 1000):
	if i%2!=0 and i%5!=0:
		print(i);
		period = count_period(i);
		print(period);
		if period > max_period:
			max_period = period;
			max_index = i;
print(max_period, max_index);