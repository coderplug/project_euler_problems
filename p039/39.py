import operator
from collections import defaultdict
result = [];
for a in range(1, 500):
	for b in range(1, 500):
		c = (a**2+b**2)**(1/2);
		if c == int(c) and a+b+c <= 1000 and a*b*0.5 == int(a*b*0.5):
			c = int(c);
			perimeter = int(a+b+c);
			area = int(a*b*0.5);
			if [b, a, perimeter] not in result:
				result += [[a, b, perimeter]];
				#print(a, b, c, perimeter, area);
#print(result);
dict = defaultdict(lambda: 0, {});
for entry in result:
	dict[str(entry[2])] += 1;
print(max(dict.items(), key=operator.itemgetter(1))[0]);
