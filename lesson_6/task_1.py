"""
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
and the number of occurrences as values.
"""
import string

unique_words = {}
user_input = "# make make. hello and and! and,I want>>wanna>>" #  input("Enter a sentence: ").strip()
words = []

print(words)
for word in words:
	if word not in unique_words:
		unique_words[word] = 1
	else:
		unique_words[word] += 1
print(unique_words)
# make make. hello and and! and,I want>>wanna>>
