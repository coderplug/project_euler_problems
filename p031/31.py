def collect_2_pounds(result, index, total):
	#print(result, index, total);
	count = 0;
	coins = [200, 100, 50, 20, 10, 5, 2, 1];
	if index < 8:
		
		maximum = int((200 - total)//coins[index]);
		#print(total, index, maximum);
		for amount in range(maximum + 1):
			#print(amount, coins[index]);
			result += [amount];
			if total + amount*coins[index] == 200:
				count += 1;
				#print(result);
			else:
				count_r = collect_2_pounds(result, index + 1, float(repr(total + amount*coins[index])));
				count += count_r;
			result.pop();
	return count;
	
print(collect_2_pounds([], 0, 0));

					
	