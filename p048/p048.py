import math

last_ten = 0
modulo = 10000000000
sum = 1
for i in range(1, 1001):
    sum = i
    for j in range(1, i):
        sum = (sum * i) % modulo
    last_ten += sum    
    print(i, " ", sum)    
print(last_ten % modulo)
input()
