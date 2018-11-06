#Needs optimization
import math
triangle = 1
number = 1
limit = 100
num_devisors = 0
while num_devisors < 500:#triangle != 100:
	#print(triangle, number)
	triangle += 1
	number += triangle
	num_devisors = 2
	for i in range(2, int(math.sqrt(number))+1): 
		if number % i == 0:
			num_devisors += 2
		if i*i == number:
			num_devisors -= 1
			#print(triangle, num_devisors)
print(triangle, number)