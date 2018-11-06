import math, io

def dict_duplicates(number_primes):
    key_value = []
    for primes in number_primes:
        for key, value in primes.items():
            if (key, value) in key_value:
                return True
            key_value.append((key, value))
    #print(key_value)
    return False

primes = []
f = open("primes.txt", "r", encoding="utf-8")
for line in f:
    for word in line.split():
       primes.append(int(word))
       
primes_in_a_row = 0
number = 2
number_primes = []
while primes_in_a_row != 4:
    #print(number)
    primes_in_a_row += 1
    dict_primes = {}
    current_prime_state = number
    while current_prime_state != 1:
        for prime in primes:
            if current_prime_state % prime == 0:
                dict_primes[prime] = (dict_primes[prime] + 1) if prime in dict_primes else 1
                current_prime_state /= prime
                break
    number_primes.append(dict_primes)
    if dict_duplicates(number_primes):
        primes_in_a_row -= 1
        #print(number_primes)
        number_primes.pop(0)
    elif len(dict_primes.items()) != 4:
        primes_in_a_row = 0
        number_primes = []
    number += 1
print(number-4)
input()
