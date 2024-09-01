# Auto Trash Cleaner - Python project , deletes automatically all files in this folder from time period between every 4 hours
# Built By - Bhavya Padaliya 
# github profile :- github.com/bhavyax7673
import winshell
import os
from time import sleep

folder = "./"

while True:
    all_files_list = os.listdir(folder) # put the location of folder you wanna use as a trash bin
    print("All Files To Be Delete :- \n")
    found = False

    for file_name in all_files_list:
        if file_name not in ["README.md",".git","main.py"]:
            found = True
            os.remove(file_name)
            print(f"{file_name}\n")

    winshell.recycle_bin().empty(True,True,True)
    print("Files Deleted Successfully")

    sleep(60*60*12)
    