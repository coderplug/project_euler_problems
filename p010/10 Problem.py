#neefektyvu!
import math
def sum_primes (limit):
	sum = 2
	for i in range(3, limit, 2):
		flag = False
		for j in range(3, int(math.sqrt(i))+1, 2):
			if i%j == 0:
				flag = True
				break
		if flag == False:
			#print(i, sum)
			sum += i
	return sum

print(sum_primes(2000000))