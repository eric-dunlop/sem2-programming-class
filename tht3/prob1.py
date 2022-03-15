
import time
import datetime
from datetime import datetime
import os
import sys
from prettytable import PrettyTable
from colorama import Fore


#=====================================================================
# filters the command line arguments/input options.
# if they are accepted return [dirpath, log, user]
# if they are not accepted print_usage is called
def get_options(input_options):
    print(f'input options: {input_options}')
    log_level_options = ['fatal', 'critical', 'warn', 'info']
    usernames = ['root', 'ubuntu', 'wheel', 'vbox', 'syslog', 'arty']
    if input_options[1] in log_level_options and input_options[2] in usernames:
    
        return input_options
    
    else:
        print_usage()
    
#=====================================================================
# print usage message and prompt to input options runs if
# current user options are not accepted 
# exit program id 'q' is input
# returns the updated user options [dirpath, log, user]
def print_usage():

    print(f'{Fore.RED} %%%%%%%% USAGE %%%%%%%%')
    print(f'\n"q" to Quit{Fore.RESET}\n')
    print('log options:\t\tfatal, critical, warn, info')
    print('Username options:\troot, ubuntu, wheel, vbox, syslog, arty')
    print('\nUsage: dir-path log username\n')
    user_input = input('---#>').split()
    if user_input == ['q']:
        exit(-1)

    elif len(user_input) < 3:
        print_usage()
    else:
        return user_input

# time, user, message, log level
#=========================================================================
# walks the selected file and updates a global log_dict of all the logs
# no return value
# log_dict{file:{log:{user:[[time, message], [...] ]}}}
def build_log_dict(file):

    with open(file, 'r') as logfile:
        current_line = logfile.readline()
        while(current_line):
            log_list = current_line.strip().split(':')
            time_str, user, message, level = [item.strip() for item in log_list]

            log_time = datetime.fromtimestamp(float(time_str))
            time_str = log_time.strftime(f'%b %d, %Y %H:%M:%S:{time_str}')

            # i think there must be a better way to build a nested dict.
            # if there is can you point me in the right direction?
            if file in log_dict:
                if level in log_dict[file]:
                    if user in log_dict[file][level]:
                        log_dict[file][level][user].append([time_str, message])

                    else:
                        log_dict[file][level][user] = [[time_str, message]]
                else:
                    log_dict[file][level] = {user:[[time_str, message]]}
            else:
                log_dict[file] = {level:{user:[[time_str, message]]}}

            current_line = logfile.readline()

#============================================================================
# user input = [filepath, log, user]
# accesses the global log_dict and parses out the requested information 
# prints table displaying all fault logs of selected type and user for each file 
# same information is savec the timestamped txt file.
def print_selection(user_input):
    global log_dict
    output_table = PrettyTable()
    output_table.hrules = True
    output_table.field_names = ['FileName', 'Log Level', 'UserName', 'Date', 'Message']
    
    filename = f'parsed_logs{time.time()}.txt'
    with open(filename, 'w') as output_file: 

        # same thing, I'm sure there is a better way to parse a nested dict
        # how?
        for file in log_dict:
            for level in log_dict[file]:
                if level.lower() == user_input[1]:
                    for user in log_dict[file][level]:
                        if user.lower() == user_input[2]:

                            dates = ''
                            messages = ''
                            output_file.write(f'{file}:{level}:{user}\n')

                            for entry in log_dict[file][level][user]:
                                dates += entry[0] + '\n'
                                messages += entry[1] + '\n' 
                                output_file.write(f'{entry[0]} % {entry[1]}\n')

                            table_row = []
                            table_row.append(file)
                            table_row.append(level)
                            table_row.append(user)

                            table_row.append(dates)
                            table_row.append(messages)
                            output_table.add_row(table_row)
                            
    print(output_table)
    print(f'created: {filename}')
#==========================================================================

log_dict = {}

input_options = sys.argv[1:]
while len(input_options) < 3:
    input_options = print_usage()

user_input = get_options(input_options)

# walk the selected directory and call build_log_dict on each file
for root, dirs, files in os.walk(user_input[0]):
    for file in files:
        build_log_dict(root + '/' + file)

print_selection(user_input)


