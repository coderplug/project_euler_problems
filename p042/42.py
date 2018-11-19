def generate_triangle_numbers(t_from, t_to):
	triangle_numbers = [];
	for i in range(t_from, t_to+1):
		triangle_numbers += [int((1/2)*i*(i+1))];
	return triangle_numbers;
def get_words_from_file(file_name):
	f = open(file_name, 'r');
	text = f.read()[1:-1];
	word_list = text.split('","');
	return word_list;
def calculate_triangle_value(word):
	word = word.lower();
	sum = 0;
	for letter in word:
		value = ord(letter) - ord('a') + 1;
		sum += value;
	return sum;
triangle_nums = generate_triangle_numbers(1, 32);
print(triangle_nums);
words = get_words_from_file("p042_words.txt");
count = 0;
for word in words:
	triangle_value = calculate_triangle_value(word);
	if triangle_value in triangle_nums:
		count += 1;
		print(word, triangle_value);
print("In given textfile triangle numbers - ", count);