'''def fibonacci(index, n_1, n_2):
	index+=1;
	print(len(str(n_1+n_2)));
	return fibonacci(index, n_2, n_1+n_2);
fibonacci(2, 1, 1);
'''
length = len(str(1));
index = 2;
n_1 = 1;
n_2 = 1;
while length < 1000:
	tmp = n_1 + n_2;
	n_1 = n_2;
	n_2 = tmp;
	index += 1;
	length = len(str(n_2));
print(index);
