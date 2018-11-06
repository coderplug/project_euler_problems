

def square_difference(number):
	sum = 0;
	square_sum_ind = 0;
	for x in range(1, number+1):
		sum += x
		square_sum_ind += x**2
	return sum**2 - square_sum_ind
	
print(square_difference(100))