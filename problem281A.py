'''
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

Output
Output the given word after capitalization.
'''

while True:
	word = input("")

	if word[0].isupper():
		print(word)
		break

	elif word[0].islower():
		print(word[0].upper() + word[1:])
		break
		
	else:
		continue
