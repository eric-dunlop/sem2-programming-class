#!/usr/bin/python3

# Filename: prob1.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  dict interprating
# Resources:https://zetcode.com/python/prettytable/
#			https://docs.python.org/3/library/ipaddress.html 
#			https://stackoverflow.com/questions/63192480/check-if-valid-ip-address-from-user-input
from prettytable import PrettyTable
import ipaddress

# some pretty tables set up
pt = PrettyTable()
pt.field_names = ["Computer Name", "Manufacturer", "Asset Tag", "IP Address", "IP Subnet", "Price"]

computer_dict = {
	"Comp477": ["Gigabyte", 9133.27, "70561924KIQqzw", "68.192.163.42/255.255.240.0"], 
	"Comp678": ["Asus", 7264.42, "56024371IQCewb", "198.78.85.109/255.255.248.0"], 
	"Comp894": ["Acer", 4564.22, "41928367UHPkxu", "192.167.55.136/255.255.240.0"], 
	"Comp592": ["Dell", 9378.82, "20451398MFWusg", "192.167.86.14/255.255.255.128"], 
	"Comp397": ["Acer", 8115.08, "74189306HKLvwu", "176.33.145.182/255.255.248.0"], 
	"Comp697": ["Asus", 8941.52, "17892534DZOlru", "10.0.252.127/255.255.192.0"], 
	"Comp966": ["Dell", 9539.92, "46193287TYIurw", "10.0.222.132/255.255.252.0"], 
	"Comp964": ["Dell", 4274.43, "04237918UTSdkj", "200.3.34.67/255.255.192.0"], 
	"Comp634": ["Google", 5182.86, "95430287FCQfbk", "68.192.177.108/255.255.192.0"], 
	"Comp565": ["Toshiba", 1904.33, "57018243JPYtpu", "192.167.63.98/255.255.240.0"], 
	"Comp906": ["Dell", 5228.37, "96134827IHGibu", "176.33.20.163/255.255.192.0"], 
	"Comp481": ["Asus", 7790.58, "05793218BRZjgl", "198.78.237.73/255.255.248.0"], 
	"Comp370": ["Dell", 9251.70, "89531276LIMqby", "68.192.129.199/255.255.192.0"], 
	"Comp703": ["Toshiba", 7520.04, "53179426FUXqjz", "200.3.191.102/255.255.192.0"], 
	"Comp493": ["Google", 4621.55, "06514398WINzou", "198.78.59.119/255.255.240.0"]
}
# I just need this later for stuff
comp_list = []
#loop formats each row of the dict
for comp in computer_dict:
	# set a variable for readability
	comp_row = computer_dict[comp]
	# make the ip object
	ip_obj = ipaddress.IPv4Network(comp_row[3], strict=False)
	# remove the subnet mask from the ip
	comp_row[3] = comp_row[3][:comp_row[3].index("/")]
	# insert the netwrok address
	comp_row.insert(4, ip_obj.network_address)
	# add the computer name to the front of the list
	comp_row.insert(0, comp)
	# move price to the end.
	comp_row.append(comp_row.pop(2))
	# add the modified lists to my list of lists
	comp_list.append(comp_row)
	# add the row to the table
	pt.add_row(comp_row)
	# sort by subnet because i thought that made sense.
	pt.sortby = "IP Subnet"
print(pt)
print("+="*45 + "+\n")

# clear the table
pt.clear_rows()
# keeps running until exited
while 1:
	print("what network would you like to locate?")
	print("format: ipadddress/subnetmask --or-- ipaddress/xx")
	network = input("q to Quit\n\n")
	# exit path
	if network == "q":
		print("%%%% Closing %%%%\n")
		exit(-1)
	# input filter 
	try:
		network = ipaddress.IPv4Network(network, strict=False).network_address
	#exit error
	except:
		print("%%%% Invalid network %%%%\n")

	# if filter passes with no errors this runs
	else:
		for comp in comp_list:
			# checking the input network against each comp_list
			if network == comp[4]:
				# add row
				pt.add_row(comp)
		print(pt)
		print("+="*45 + "+\n")





