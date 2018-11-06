

def largest_palindrome (first, second):
	largest = 0
	for i in range(first, 99, -1):
		for j in range(second, 99, -1):
			n = i*j
			if str(n) == str(n)[::-1] and largest < n:
				largest = n
	return largest

print(largest_palindrome(999, 999))