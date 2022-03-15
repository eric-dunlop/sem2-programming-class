#!/usr/bin/python3

# Filename: prob1.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  investigating pefiles
# references:

# get the user inputs
# returns [requested strlen, address size]

def get_settings():
	# usage message
	usage = "%%% USAGE %%% random string length must be in the range 100 - 1024\n%%% USAGE %%% address size must be 4 or 8"
	
	strlen = int(input("How long should the random string be? "))
	print()
	# filters the input
	if not strlen >= 100 or not strlen <= 1024:
		print(usage)
		exit(1)

	addsize = int(input("What size address are we dealing with? "))
	# filters the input
	if not addsize == 4 and not addsize == 8:
		print(usage)
		exit(1)
		
	return [strlen, addsize]
	
#===================================================================		
# generates a non repeating string of inputlength
# returns the generated string	
#		Llnl

def generate_string(length):
	longstr = ''
	toadd = ''
	char1 = 0x41
	char2 = 0x61
	char3 = 0x30
	char4 = 0x61

	# makes the srting at least long enough
	for i in range(length//4+4):
		toadd = chr(char1) + chr(char2) + chr(char3) + chr(char4)
		longstr += toadd
		char1 += 1
		if char1 > 0x5A:
			char1 = 0x41
			char2 += 0x1

		if char2 > 0x7A:
			char2 = 0x61
			char3 += 1
			
		# I included the symbols on purpose , not a hex mistake	
		if char3 > 0x40:
			char3 = 0x30
			char4 += 1
			
		if char4 > 0x7E:
			char4 = 0x20
	#trims the string to the exact length requested
	longstr = longstr[:length]
	print("\n" + longstr,"\n")
	return longstr
	
#================================================================================
# searches the for the requested string within the generated string 
# prints the index of the requested string
# no return 

def search_string(longstr):

	substring = input("What string would you like to locate? ")
	located_index = longstr.find(substring)
	# exit the program here
	if substring == "q": exit(1)	
	if located_index == -1:	
		print("\n%%% sorry, your string could not be located %%%")	
		print("\nEnter q to Quit\n")
	else:
		print("\nThe seaquence ", substring, " starts at index: ",located_index)
		print(f"The string was found {longstr.count(substring)} time(s).")
		print("+-"*20 + "+\n")
		
#==================================================================================	
# main 
	
user_settings = get_settings()

longstr = generate_string(user_settings[0])

while True:
	search_string(longstr)




