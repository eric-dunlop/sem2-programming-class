#!/usr/bin/python3

# Filename: prob1.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  keywords list
# Resources:

from keyword import kwlist

longest_word = 0
# sort the list
keywords_sorted = sorted(list(kwlist), key=str.lower)

# remove any that stat with __
for word in keywords_sorted:
	if word[0] == "_":
		keywords_sorted.remove(word)
		continue
		
	# find the len of the longest word
	if len(word) > longest_word:
		longest_word = len(word)
		
# prints the formatted output
print("+="*26)
for i in range(len(keywords_sorted)-1):
	print(keywords_sorted[i].rjust(longest_word + 2), sep="", end="")
	if i % 5 == 4:
		print()
print()
print("+="*26 + "+\n")

