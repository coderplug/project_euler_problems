file = open("p022_names.txt");
letters = {}
letters['A'] = 1
letters['B'] = 2
letters['C'] = 3
letters['D'] = 4
letters['E'] = 5
letters['F'] = 6
letters['G'] = 7
letters['H'] = 8
letters['I'] = 9
letters['J'] = 10
letters['K'] = 11
letters['L'] = 12
letters['M'] = 13
letters['N'] = 14
letters['O'] = 15
letters['P'] = 16
letters['Q'] = 17
letters['R'] = 18
letters['S'] = 19
letters['T'] = 20
letters['U'] = 21
letters['V'] = 22
letters['W'] = 23
letters['X'] = 24
letters['Y'] = 25
letters['Z'] = 26
names = file.readline()
names = names.lstrip('"')
names = names.rstrip('"')
names = names.split('","')
names.sort()
total = 0
for i in range(0, len(names)):
	sum = 0
	for j in names[i]:
		sum += letters[j]
	sum *= (i+1)
	if names[i] == 'COLIN':
		print(i+1, sum)
	total += sum
print(total)