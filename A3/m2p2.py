#!/usr/bin/python3

# Filename: prob1.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  sorting files by date
# reference: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
#			 https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
#			 https://stackoverflow.com/questions/40445258/problems-using-colorama-on-python-2-7


import os, time
from datetime import datetime
from colorama import Fore,Style


#======================================================================
# prints the user input file tree

def display_tree(input_dir):
	for root, dirs, files in os.walk(input_dir):
		print(Fore.RED + "\n" + root + Style.RESET_ALL)
		for f in files:
			print("\t--",f)

#=====================================================================
# accepts a user input date range and prints the values modified within the range
# no return value

def display_daterange(input_dir):
	reject_list = []
	# loops until it gets a valid input
	while True:	
		input_range = input("\nEnter file date range YYYY/MM/DD-YYYY/MM/DD to filter for: ")
		print("+="*39 +"+")
		input_range = "2000/10/02-2010/10/02"
		try:
			start_date = datetime.strptime(input_range.split("-")[0], "%Y/%m/%d")
			end_date = datetime.strptime(input_range.split("-")[1], "%Y/%m/%d")
		except:
			print("\ninvalid date format")	
		else:
			break
	# check each file against the daterange and print the files that are in it
	for root, dirs, files in os.walk(input_dir):
		for f in files:
			path = root + "/" + f
			modtime = time.ctime(os.path.getmtime(path))
			modtime = datetime.strptime(modtime, "%a %b %d %X %Y")
			if start_date <= modtime <= end_date:
				print(Fore.RED + root + "/" + Style.RESET_ALL + f, end="")
				print(Fore.BLUE + "\t\tDate: ", datetime.strftime(modtime, "%b %d, %Y - %X"))
			else:
				reject_list.append(root + "/" + f + "\t\tDate: " + datetime.strftime(modtime, "%b %d, %Y - %X"))
	print(Style.RESET_ALL + "+="*39 +"+" + "\n" + Fore.YELLOW + "\nrejected files:")
	print(Fore.YELLOW)
	for reject in reject_list:
		print(reject)

#===============================================================================

input_dir = input("What folder would you like to analyze? ")

input_dir = "Lab3_ITSC203"
display_tree(input_dir)

display_daterange(input_dir)





