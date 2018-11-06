import time
import math

a = 3
b = 5
limit = 1000
#Solution 1
start = time.clock()
sum = 0
for x in range (a, limit):
	if x % a == 0 or x % b == 0:
		sum += x
		#print(x)
print(sum)
end = time.clock()
print("1st Finished in ", end - start)
#Solution 2 (Not fully works)
start = time.clock()
sum = 0
both = set()
for x in range (1, math.floor(limit/a)):
	sum += x*a
for x in range (1, math.floor(limit/b)):
	sum += x*b
	if x*b%a == 0:
		both.add(x*b)
for x in both:
	sum -= x
print(sum)
end = time.clock()
print("2nd Finished in ", end - start)
#Solution 3 (Mathematical)
start = time.clock()
sum = 0
a_mult = math.floor(limit/a)
b_mult = math.floor(limit/b)
ab_mult = math.floor(limit/(a*b))
sum += a_mult*a*(a_mult + 1)
sum += b_mult*b*(b_mult + 1)
sum -= ab_mult*a*b*(ab_mult + 1)
"""
if a%b != 0 and b%a != 0:
	sum -= math.floor(limit/(b*a))*a*b*(math.floor(limit/(b*a)) + 1)
elif a%b == 0:
	sum -= math.floor(limit/a)*a*(math.floor(limit/a) + 1)
elif b%a == 0:
	sum -= math.floor(limit/b)*b*(math.floor(limit/b) + 1)
"""
print(int(sum/2)) #nes kitur nedalinu is 2
end = time.clock()
print("3rd Finished in ", end - start)
#Solution 4 (Mathematical, knowing amounts)
start = time.clock()
sum = 0
sum += 333*(a+999)/2
sum += 200*(b+1000)/2
sum -= 66*(15+990)/2
print(int(sum))
end = time.clock()
print("4th Finished in ", end - start)