import math

def list_to_integer(numList):
    s = ''.join(map(str, numList))
    return int(s)

def get_replaced_digits(digits, start, digits_count, positions):
    #print(digits)
    length = len(digits)
    if digits_count == 0:
        list = []
        for i in range(10):
            new_digits = digits.copy()
            if i == 0 and 0 in positions:
                continue
            for pos in positions:
                new_digits[pos] = i
            list.append(list_to_integer(new_digits))
        return [list]
    limit = length+1-digits_count
    digits_list = []
    for i in range(start, limit):
        positions.append(i)
        digits_list += get_replaced_digits(digits, i+1, digits_count-1, positions)
        positions.remove(i)
    return digits_list
    
    
def list_replaced_digits(number):
    digits = [int(d) for d in str(number)]
    length = len(digits)
    list = []
    for dig_count in range(1, length):
        numbers = get_replaced_digits(digits, 0, dig_count, [])
        list += numbers
    return list

def get_primes():
    primes = []
    f = open("primes.txt", "r", encoding="utf-8")
    for line in f:
        for word in line.split():
            primes.append(int(word))
    return primes

    '''
def find_eight_prime_combo(primes):
    for prime in primes:
        for collection in list_replaced_digits(prime):
            count = 0
            for number in collection:
                if number in primes:
                    count += 1
            print(collection)
            print(count)
            #if count == 8:
                #return prime
'''
def find_eight_prime_combo(primes, num):
    for collection in list_replaced_digits(num):
        count = 0
        for number in collection:
            if number in primes:
                count += 1
        print(collection)
        print(count)  
        if count == 7:
            return number
    
primes = get_primes()
print(find_eight_prime_combo(primes, 56003))
input()
