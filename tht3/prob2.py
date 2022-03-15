
from operator import index
import os
import datetime
from datetime import datetime
from colorama import Fore, Back, init


#===================================================================
# Input: The function takes as input the directory to analyze
# Output: The function returns a dictionary, with the log file, its path and timestamp
# provided with assignment
def getloginfo(directory):
    file_dict = {}
    for path, folder, files in os.walk(directory): 
        for afile in files:
            if os.path.splitext(afile)[1] == '.log':
                file_dict.setdefault(afile, [])
                answer = path + '_' + str(os.path.getmtime(path + '/' + afile))
                file_dict[afile].append(answer)

    return file_dict

#=======================================================================
# parses and print the information from the dict provided by getlogin info 
# unfortinatly on my VM there was not much usable unformation in the .log files 
# see other functions that filter information from some log files I found in the system
def parse_garys_dict(file_dict):
    for file in file_dict:
        time_stamp = datetime.fromtimestamp(float(file_dict[file][0].split('_')[1]))
        print(Fore.MAGENTA + file_dict[file][0].split('_')[0] + '/' + file)
        print(f'{Fore.LIGHTCYAN_EX}{time_stamp}')
        print()

#=============================================================================
# scans the file and filters for records containing any of the words in supplied list 
# prints all hits with the located word highlighted
# prints the newest and oldest logs in the file 
# works on any log that starts wit a date format '%Y-%m-%d %H:%M:%S'
def check_log(filepath):
    
    log_file = open(filepath, 'r')
    newest_log_time = datetime.fromtimestamp(0)
    oldest_log_time = datetime.now()
    newest_log = ''
    oldest_log = ''
    word_list = ['Error', 'Warning', 'Fail', 'Crash', 'Failure']
    log_entry = log_file.readline()

    while log_entry:

        log_time = datetime.strptime(log_entry[:19], '%Y-%m-%d %H:%M:%S')
        #print(log_time)

        if log_time > newest_log_time and not '===' in log_entry:
            newest_log_time = log_time
            newest_log = log_entry  

        if log_time < oldest_log_time and not '===' in log_entry:
            oldest_log_time = log_time
            oldest_log = log_entry
        
        for word in word_list:
            if word.lower() in log_entry.lower():
                print(log_entry[:log_entry.lower().index(word.lower())], end='')
                print(f'{Fore.RED}{word}',end='')
                print(log_entry[log_entry.lower().index(word.lower()) + len(word):],end = '')

        log_entry = log_file.readline()

    print(f'{Fore.MAGENTA}newest log in {filepath}: \n{Fore.RESET}{newest_log}', end = '') 
    print(f'{Fore.CYAN}{newest_log_time}\n')
    print(f'{Fore.MAGENTA}oldest log in {filepath}: \n{Fore.RESET}{oldest_log}', end = '')
    print(f'{Fore.CYAN}{oldest_log_time}\n') 
    
    log_file.close()

    input('Press Enter to continue\n')

#==========================================================================
# very similar to the check_log() function different date format in the alt log
def check_alt_log(filepath):
    
    log_file = open('/var/log/alternatives.log.1', 'r')
    newest_log_time = datetime.fromtimestamp(0)
    oldest_log_time = datetime.now()
    newest_log = ''
    oldest_log = ''
    word_list = ['Error', 'Warning', 'Fail', 'Crash', 'Failure']
    log_entry = log_file.readline()

    while log_entry:
        print(log_entry)
        log_time = datetime.strptime(log_entry.split()[1] + log_entry.split()[2], '%Y-%m-%d%H:%M:%S:')

        if log_time > newest_log_time:
            newest_log_time = log_time
            newest_log = log_entry

        if log_time < oldest_log_time:
            oldest_log_time = log_time
            oldest_log = log_entry
        
        for word in word_list:
            if word.lower() in log_entry.lower():
                print(log_entry[:log_entry.lower().index(word.lower())], end='')
                print(f'{Fore.MAGENTA}{word}',end='')
                print(log_entry[log_entry.lower().index(word.lower()) + len(word):],end = '')

        log_entry = log_file.readline()

    print(f'{Fore.MAGENTA}newest log in {filepath}: \n{Fore.RESET}{newest_log}', end = '') 
    print(f'{Fore.CYAN}{newest_log_time}\n')
    print(f'{Fore.MAGENTA}oldest log in {filepath}: \n{Fore.RESET}{oldest_log}', end = '')
    print(f'{Fore.CYAN}{oldest_log_time}\n') 
    
    log_file.close()

    input('Press Enter to continue\n')

#===========================================================================
# dpkg.log.1
# lynis.log
# alternatives.log.1
init(autoreset=True)

file_dict = getloginfo('/var/log')
parse_garys_dict(file_dict)

check_alt_log('/var/log/alternatives.log.1')
check_log('/var/log/lynis.log')
check_log('/var/log/dpkg.log.1')
