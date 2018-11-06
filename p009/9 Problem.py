#GALIMA EFEKTYVIAU, LABAI BRUTE
def pythag_triplet (sum):
	for i in range (0, sum):
		for j in range(0, i):
			for k in range(0, j):
				if i+j+k == sum and k**2 + j**2 == i**2:
					return i*j*k

print(pythag_triplet(1000))