import sys
def isprime(n):
    """Returns True if n is prime."""
    if n < 2:
        return False
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
def generate_primes(count):
	l_count = 1;
	primes = [2];
	for i in range(3, sys.maxsize**10, 2):
		if l_count >= count:
			break;
		if isprime(i):
			l_count += 1;
			primes += [i];
	return primes;
def generate_squares(index_from, index_to):
	squares = []
	for i in range(index_from, index_to+1):
		squares += [i**2]
	return squares;
def generate_odds(index_from, index_to):
	odds = [];
	for i in range(index_from, index_to+1, 2):
		if i%2==1:
			odds += [i];
	return odds;
primes = generate_primes(1000);
squares = generate_squares(1, 1000);
odds = set(generate_odds(3, 999999));
oddies = set();
for prime in primes:
	for square in squares:
		oddies.add(prime+2*square);
odds = list(odds.difference(oddies));

odds.sort(reverse=False);
result = []
for odd in odds:
	if isprime(odd) is False:
		result += [odd]
print(result[0], result[1]);