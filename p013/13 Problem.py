with open("numbers.txt") as f:
	new_content = f.readlines()
num_array = [int(i) for i in new_content]
print(repr(sum(num_array))[:10])