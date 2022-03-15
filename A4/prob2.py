#!/usr/bin/python3

# Filename: prob2.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  pexpect
# references:   
#   

import pexpect
from random import randint
import string
from colorama import Fore, init
init(autoreset=True)


#=============================================================
# generates a randome 8 digit password of [a-zA-Z0-9]
# returns the password as a string
def create_password():
    password = ''
    digits = string.ascii_letters +string.digits
    while len(password) < 8:
        # if randint(30,122)
        password += digits[(randint(0,len(digits)-1))]
    return password

#==============================================================
# handles the opening instructions of testlogin.out
# returns complete users as a list.
def get_users(child):

    child.expect('Press Enter to continue:')
    child.sendline('')
    child.expect('Press Enter to continue:')
    # gets the users out of the program
    # I did this before you showed us the cool .decode() thing
    users = str(child.before)
    users = users.split('\\r\\n\\t\\t')
    users.pop(0)
    users[4] = users[4][:-12]
    child.sendline('')
    return users

#==============================================================
# takes each user from a list, extracts the username and tries 
# randome passwords until it gets 2 hits
# prints every try because it makes me feel like a hacker
# returns user_dict{'username':{'proper name':[password, ... ,]}}
def scan_users(users):
    user_dict = {}
    name = ''
    password = ''
    counter = 0

    for user in users:
        user = user.split()
        userid = user[3][:user[3].find('@')]
        user_dict[userid] = {user[1] + ' ' + user[2]:[]}
        pass_counter = 2

        while pass_counter:
            child.expect(': ')
            prompt = child.before.decode().split()[-1]

            if prompt == 'choice':
                print(f'user: {userid}\npassword: {password}')
                for key in user_dict[userid]:
                    name = key
                    user_dict[userid][name].append(password)
                    print(f'{Fore.RED} %%%% HIT!!!!! %%% {Fore.RESET}')
                    child.sendline('Y')
                pass_counter -= 1

            elif prompt == 'username':
                counter += 1
                print(f'userid\t == {userid}')
                child.sendline(userid)

            elif prompt == 'password':
                password = create_password()
                child.sendline(password)
                print(f'password == {password}\t attempt number: {counter}')
    return user_dict

#==============================================================
# prints a pretty output. easy to parse > passwords.txt
# username:First Last:password1,password2,...
# no return value 
def save_results(user_dict):

    with open('passwords.txt', 'w') as password_file:
        print('\n\n' + Fore.RED + '+='*12 + '+')
        password_file.write('+='*12 + '+\n')

        for user in user_dict:
            print(f'{Fore.CYAN}Username:\t{Fore.YELLOW + user}')
            password_file.write(f'{user}:')
            for key in user_dict[user]:
                password_file.write(f'{key}:')
                for password in user_dict[user][key]:
                    print(f'{Fore.LIGHTWHITE_EX}Password:\t{Fore.GREEN + password}')
                    password_file.write(f'{password},')
            password_file.write('\n')
            print(Fore.RED + '+='*12 + '+')
            
#===============================================================
child = pexpect.spawn('./testlogin.out')
# who has time to wait 0.05 of a second every try?
child.delaybeforesend = 0
child.timeout = 31
users = get_users(child)
user_dict = scan_users(users)       
save_results(user_dict)




