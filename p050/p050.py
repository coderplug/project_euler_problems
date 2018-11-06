import math

def get_primes():
    primes = []
    f = open("primes.txt", "r", encoding="utf-8")
    for line in f:
        for word in line.split():
            primes.append(int(word))
    return primes

def cumulative_sum(primes):
    c_sum = []
    for prime in primes:
        if prime == primes[0]:
            next_member = prime
        else:
            next_member = c_sum[-1] + prime
        c_sum.append(next_member)
    return c_sum
    
primes = get_primes()
limit = 1000000
c_sum = cumulative_sum(primes)
#print(c_sum)
max = 0, 0, 0
for i in range(0, len(c_sum)):
    for j in range((i-1), -1, -1):
        count = i-j
        new_sum = (c_sum[i]-c_sum[j])
        if new_sum > limit:
            break
        elif count >= (max[1]-max[2]) and new_sum in primes:
            if count == (max[1]-max[2]):
                if new_sum > max[0]:
                    max = new_sum, i, j
            else:
                max = new_sum, i, j
print(max)
input()
