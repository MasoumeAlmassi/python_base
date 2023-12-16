sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(f'The original sentence is: {sentence}')

sentence = sentence.replace("!"," ")
print(f'Replacing ! with spaces, the sentence is now: {sentence}')


sentence = sentence.upper()
print(f'Converting the sentence to upper case, the sentence is now: {sentence}')

sentence = sentence[::-1]
print(f'Printing in reverse by a backward slice function, the sentence is now: {sentence}')