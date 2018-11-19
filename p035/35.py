def get_number(dig_list):
	index = 0;
	number = 0;
	for digit in dig_list:
		index+=1;
		number += digit*10**(len(dig_list)-index);
	return number;
def get_digits(n):
	digits = [];
	while n:
		digits = [n % 10] + digits;
		n = n // 10;
	return digits;
def rotate(dig_list): 
	moving_digit = dig_list.pop();
	dig_list = [moving_digit] + dig_list;
	return dig_list;
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
primes = [];
circular_primes = [];
for i in range(2, 1000000):
	if isprime(i) is True:
		primes += [i];
#print(primes);
for prime in primes:
	digits = get_digits(prime);
	rotated_prime = list(digits);
	circular = True;
	for index in range(1, len(digits)):
		rotated_prime = rotate(rotated_prime);
		#print(prime, rotated_prime);
		if get_number(rotated_prime) not in primes:
			circular = False;
			break;
	if circular is True:
		circular_primes += [prime];
print(circular_primes);
print(len(circular_primes));