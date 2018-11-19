def form_number(number, all, count):
	new_range = [x for x in all if x not in number];
	#print(len(new_range));
	if(len(new_range) == 0):
		#print(number);
		count+=1;
		#print(count);
		if(count == 1000000):
			return number, count;
	else:
		position = len(number);
		for i in new_range:
			number += [i];
			#print(number);
			result, count = form_number(number, all, count);
			if result is not False:
				return result, count;
			number.pop();
	return False, count;

list = range(10);
result, count = form_number([], list, 0);
print(result);