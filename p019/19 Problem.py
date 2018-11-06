days_year = {}
first_sunday = 6
sundays = 0
first_leap = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
first_non_leap = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
for i in range(1901, 2001):
	if i % 4 == 0 and i % 100 != 0:
		days_year[i] = 366
		current_year = first_leap
	elif i % 100 == 0 and i % 400 == 0:
		days_year[i] = 366
		current_year = first_leap
	else:
		days_year[i] = 365
		current_year = first_non_leap
	while first_sunday <= days_year[i]:
		if first_sunday in current_year:
			sundays += 1
		first_sunday += 7
	first_sunday -= days_year[i]
print(sundays)