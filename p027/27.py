import sys
def isprime(n):
    """Returns True if n is prime."""
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

def find_cons_primes(a, b):
	count = 0;
	for i in range(0, sys.maxsize**10):
		number = i**2 + a*i + b;
		if number < 0:
			return 0;
		if isprime(number) is False:
			#print(a, b, count);
			return count;
		count += 1;
	return count;
max=0;
product=0;
for a in range(-999, 1000):
	print(a);
	for b in range(-1000, 1001):
		count = find_cons_primes(a, b);
		if max < count:
			print(a, b, count);
			max = count;
			product = a*b;
print(product);