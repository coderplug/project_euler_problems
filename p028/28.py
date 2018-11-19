def diagonal_sum(square_size):
	if square_size == 1:
		return 1;
	else:
		dist = square_size - 1;
		diag_sum = 4*square_size**2 - 6*dist;  
		return diag_sum + diagonal_sum(square_size-2);
print(diagonal_sum(1001))