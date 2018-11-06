import math

def are_primes(numbers, primes):
    for number in numbers:
        if number not in primes:
            return False
    return True

def are_permutations(numbers):
    digits = [int(d) for d in str(numbers[0])]
    for number in numbers:
        for d in str(number):
            if int(d) not in digits:
                return False
    return True

primes = []
f = open("primes.txt", "r", encoding="utf-8")
for line in f:
    for word in line.split():
       primes.append(int(word))
       
for i in range(1000, 3340):
    numbers = [i, i+3330, i+6660]
    if are_primes(numbers, primes) and are_permutations(numbers):
        print(numbers)
input()
    