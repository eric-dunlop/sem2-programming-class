#!/usr/bin/python3

# Filename: prob1.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  first python 
# Resources: https://www.programiz.com/python-programming/methods/string/center



long_name = 0
long_dir = 0
mylist = [['kenney rogers', '/home/users/KRogers'],
			['tony robbins', '/home/TRobbins'],
			['johnny cash', '/home/users/JCash'],
			['tito jockson', '/home/hut/TJackson'],
			['tim tzuyu', '/home/users/TTzuyu'],
			['kareena kapoor', '/home/users2/KKapoor']]
# get the lengnth of longest name
for name in mylist:
	if len(name[0]) > long_name:
		long_name = len(name[0])         
# get the length of longest file path 
	if len(name[1]) > long_dir:
		long_dir = len(name[1])
print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
# prints each line with title case and formatting added
for name in mylist:
	print("|", name[0].center(long_name).title(), "|", name[1].center(long_dir), "|")
print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")


