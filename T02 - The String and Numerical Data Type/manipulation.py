str_manip = input("Please enter a sentence.")
print(f'The length of this sentence is {len(str_manip)} characters.')

last_char = str_manip[-1:]
print(f'The last character in this sentence is [{last_char}].')

replace_last_char = str_manip.replace(last_char,"@")
print(f'Let us replace the last character [{last_char}] with [@] to make a new sentence: {replace_last_char}')

last_three_reversed = str_manip[-3:][::-1]
print(f'If we take the last 3 characters of the sentence and reverse them, it reads as: {last_three_reversed}.')

first_three = str_manip[0:3]
last_two = str_manip[-2:]
five_letter_word = first_three + last_two
print(f'Through the magic of Python and my personal genius, we have created a new word: {five_letter_word}.')