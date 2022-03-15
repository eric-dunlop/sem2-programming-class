#!/usr/bin/python3

# Filename: prob1.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  investigating maliciouse files
# references:   https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
#               https://www.includehelp.com/python/copy-and-rename-files.aspx

import os
from prettytable import PrettyTable
import hashlib
import shutil
#==============================================================
# creates a table of the file structure and hashes 
# copy the files to a new directory tree and organize by extension

def copy_and_display_files(input_dir):
    # set up the table
    file_table = PrettyTable(hrules = True)
    file_table.field_names = ["Directory", "File Name", "Sha256 Hash", "Files in dir"]

    for root, dirs, files in os.walk(input_dir):
        # create the variables needed for each dir.
        to_add = []
        file_string = ""
        hash_strings = ""
        
        for file in files:
            # create the variables needed file
            suffix = file.split(".")[1]
            file_string += file + "\n"
            file_src = root + "/" + file
            dest = "." + "/" + "Lab4_FileExt/" + suffix

            # create the file hash
            with open(file_src, "rb") as f:
                hash_string = hashlib.sha256(f.read()).hexdigest()
            hash_strings += hash_string +"\n"
            
            # copy, and rename the file with the hash and extension
            shutil.copy(file_src,dest)
            os.rename(dest + "/" + file, dest + "/" + hash_string + "." + suffix)
        
        #creat a string to add to the table showing the files.
        to_add.append(root)
        to_add.append(file_string)
        to_add.append(hash_strings)
        to_add.append(len(files))
        file_table.add_row(to_add)

    print(file_table)

#==============================================================
# function to create the Lab4_FileExt dir and the sundirectories for extensions
# no return value

def mk_suffix_dirs(input_dir):
    
    extensions_list = []
    # make the lab dir
    working_dir = os.getcwd() + "/Lab4_FileExt"
    try:
        os.mkdir(working_dir)
    except:
        pass
    print(working_dir)

    # make a list of all the extensions
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            extensions_list.append(file[file.find(".")+1:]) 
    # noe its a set
    extensions_set = set(extensions_list)

    # make a dir for each found extension
    for extension in extensions_set:
        try:
            os.mkdir(working_dir + "/" + extension)
        except:
            pass

#=================================================================


mk_suffix_dirs("folder079")
copy_and_display_files("folder079")





