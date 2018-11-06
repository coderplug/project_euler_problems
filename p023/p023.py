import math
#gauti visus abundant numberius
#paskaiciuot visas 2 abundant sumas
#sudet visas reiksmes neineinancias i 2 abundant sumas
#>28123 visus isreiskiam per sumas
abundant_numbers = []
two_abundant = set()
for i in range(1, 28124):
	sum = 1
	for j in range(2, int(math.sqrt(i))+1):
		if i%j == 0:
			sum += j
			sum += i//j
	if int(math.sqrt(i))**2 == i:
		sum -= int(math.sqrt(i))
	if sum > i:
		abundant_numbers.append(i)
for i in range(0, len(abundant_numbers)):
	for j in range(i, len(abundant_numbers)):
		if abundant_numbers[i] + abundant_numbers[j] > 28123:
			break
		two_abundant.add(abundant_numbers[i] + abundant_numbers[j])
#for i in two_abundant:
#	print(i)
result = 0
for i in range(1, 28124):
	if i not in two_abundant:
		result += i 
print(result)