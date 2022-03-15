#!/usr/bin/python3

# Filename: prob1.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  flow control
# Resources:

# program starts
print("this is the start of a program")
keep_running = "y" 

# loops the program until the user exits
while keep_running == "y":
	mynum = 11
	
	# loop to keep trying until a number between 0 and 10 inclusive is input
	while mynum < 0 or mynum > 10:
		mynum = int(input("\nplease input a number between 0 and 10-->> "))
		print("+="*22 + "+\n")
		
	# prints all the squares 0 - input number
	for numb in range(mynum+1):
		print("This is loop {loop_count}: {numb} squared is {squared}".format
		(loop_count=numb+1, numb=numb, squared=numb**2))
	print("\n")
	
	# input to continue or exit, any input except "y" will exit 
	keep_running = input("would you like to play again? (y/n) -->> ")

print("\n--->> PROGRAM TERMINATING <<---\n")
 
