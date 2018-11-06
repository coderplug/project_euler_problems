letters = 0
dictionary = {}
dictionary[1] = 'one'
dictionary[2] = 'two'
dictionary[3] = 'three'
dictionary[4] = 'four'
dictionary[5] = 'five'
dictionary[6] = 'six'
dictionary[7] = 'seven'
dictionary[8] = 'eight'
dictionary[9] = 'nine'
dictionary[10] = 'ten'
dictionary[11] = 'eleven'
dictionary[12] = 'twelve'
dictionary[13] = 'thirteen'
dictionary[14] = 'fourteen'
dictionary[15] = 'fifteen'
dictionary[16] = 'sixteen'
dictionary[17] = 'seventeen'
dictionary[18] = 'eighteen'
dictionary[19] = 'nineteen'
dictionary[20] = 'twenty'
dictionary[30] = 'thirty'
dictionary[40] = 'forty'
dictionary[50] = 'fifty'
dictionary[60] = 'sixty'
dictionary[70] = 'seventy'
dictionary[80] = 'eighty'
dictionary[90] = 'ninety'
dictionary[100] = 'hundred'
dictionary[1000] = 'thousand'
dictionary[-1] = 'and'
for i in range(1, 1001):
	letters_in_number = letters
	if i <= 20: #veikia
		letters += len(dictionary[i])
	elif i in range(21, 100):
		if i % 10 != 0:
			 letters += len(dictionary[i%10])
		letters += len(dictionary[i - i % 10])
	elif i in range(100, 1000):
		letters += len(dictionary[100]) # hundred
		if i%100 != 0 and i%100 > 20: # _21 - _99
			letters += len(dictionary[-1]) # and
			letters += len(dictionary[i%100 - i % 10]) # tens
			if i % 10 != 0:
				letters += len(dictionary[i%10]) # ones
		elif i%100 != 0 and i%100 <= 20: # _01-_20
			letters += len(dictionary[-1]) # and
			letters += len(dictionary[i%100]) # _01 - _20
		letters += len(dictionary[i//100])
	elif i == 1000:
		letters += len(dictionary[i]) + len(dictionary[1])
	print(i, letters - letters_in_number)
print(letters)