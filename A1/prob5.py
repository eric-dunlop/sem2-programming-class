#!/usr/bin/python3


# Filename: prob5.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  first python 
# Resources: Codecademy



int_var1 = [1, 2, 3, 4]
# fixed quotes (quotes must match)
# added space at the end so print on line 30 looks better
str_var1 = "This is a string "
# removed quotes to make it a float not a string
flt_var1 = 123.445
tup_var1 = tuple(int_var1)
# fixed the int variable names and added [] to add each index from the list
# started accumulating in sumflt instead of just changing it 
sumflt = flt_var1 + int_var1[0]
sumflt += int_var1[1]
sumflt += int_var1[2]	
sumflt += int_var1[3]
# modified the list instead of the tuple because tuples are immutable
int_var1[0] = 2
# changed print statments to use , instead of + 
# removed extra white space since print adds it at the ,s
print("sumflt is:", sumflt)
# the , adds the space, made flt_var1 a string so the statement is correct
print(str_var1, str(flt_var1))
# removed extra space added : cause i think it looks nicer
print("str_var1 * 4:", str_var1 * 4)
# made the last 4 a string so it would print without error 
print("str_var1 + 4:", str_var1 + str(4))

