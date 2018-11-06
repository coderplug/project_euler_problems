def fibonacci_sum (lim):
	a = 1
	b = 2
	sum = b
	while a+b<lim:
		c = b
		b = a + b
		a = c
		if b % 2 == 0:
			sum += b
	return sum

limit = 4000000
print("Sum of", limit, "-", fibonacci_sum(limit))
