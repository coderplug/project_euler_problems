import sys
def strip_number(to_right, number):
	if number > 9:
		if to_right is True:
			return int(str(number)[1:])
		else:
			return int(str(number)[:-1])
	else:
		print("Number cannot be stripped");
def isprime(n):
    """Returns True if n is prime."""
    if n < 2:
        return False;
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
primes = [];
strippable_primes = [];
count = 0;
for i in range(10, 1000000):
	#if count >= 11:
	#	break;
	if isprime(i) is True:
		primes += [i];
		stripped_prime_to_left = i;
		stripped_prime_to_right = i;
		strippable_prime_to_left = True;
		strippable_prime_to_right = True;
		while stripped_prime_to_left > 9:
			stripped_prime_to_left = strip_number(False, stripped_prime_to_left);
			if isprime(stripped_prime_to_left) is False:
				strippable_prime_to_left = False;
				break;
		if strippable_prime_to_left is True:
			while stripped_prime_to_right > 9:
				stripped_prime_to_right = strip_number(True, stripped_prime_to_right);
				if isprime(stripped_prime_to_right) is False:
					strippable_prime_to_right = False;
					break;
			if strippable_prime_to_right is True:
				count += 1;
				#print(i);
				strippable_primes += [i];
print(strippable_primes, sum(strippable_primes));
result = [];
for prime in strippable_primes:
	not_subnumber = True;
	for another_prime in strippable_primes:
		if str(prime) in str(another_prime) and str(prime) != str(another_prime):
			not_subnumber = False;
	if not_subnumber is True:
		result += [prime];
print(result, sum(result));