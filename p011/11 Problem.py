
#num_array = 20 * [20 * [0]]
maximum = 0
with open("numbers.txt") as f:
	new_content = [i.split() for i in f.readlines()]
#num_array
num_array = [[int(j) for j in i] for i in new_content]
for i in range(0, 19):
	for j in range(0, 19):
		number = 0
		if i<17:
			list = []
			list.append(num_array[i][j]*num_array[i+1][j]*
				num_array[i+2][j]*num_array[i+3][j])# |	
			if j in range(3, 16):
				list.append(num_array[i][j]*num_array[i+1][j-1]* 
					num_array[i+2][j-2]*num_array[i+3][j-3]) # /
				list.append(num_array[i][j]*num_array[i+1][j+1]*
					num_array[i+2][j+2]*num_array[i+3][j+3]) # \
				list.append(num_array[i][j]*num_array[i][j+1]*
					num_array[i][j+2]*num_array[i][j+3]) # -
			elif j in range(17, 19):
				list.append(num_array[i][j]*num_array[i+1][j-1]* 
					num_array[i+2][j-2]*num_array[i+3][j-3]) # /
			elif j in range(0, 2): #or simply 'else:'
				list.append(num_array[i][j]*num_array[i+1][j+1]*
					num_array[i+2][j+2]*num_array[i+3][j+3]) # \
				list.append(num_array[i][j]*num_array[i][j+1]*
					num_array[i][j+2]*num_array[i][j+3]) # -
			number = max(list);
		else:
			if j in range(0, 16):
				number = (num_array[i][j]*num_array[i][j+1]*
					num_array[i][j+2]*num_array[i][j+3])
		if number > maximum:
			maximum = number
			#elif j in range(17, 19): #not needed
				
print(maximum)
		