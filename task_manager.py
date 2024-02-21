'''This is file 1/3 of the task manager program, and should be placed in the
same directory as:
- task_manager.py (MAIN FILE) (THIS FILE)
- report_management.py
- task_management.py

The task management functions have been moved to a separate file in an attempt
to make the code more modular and to avoid having all the code in one 
congested file.
'''

# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

# Importing necessary libraries
import os
from datetime import datetime, date
from task_management import (reg_user, add_task, view_all, view_mine, manage_task,
                            generate_task_report, generate_user_report)
from report_management import display_task_report, display_user_report

# Define a constant for date time string format
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Check if tasks.txt file exists, if not, create it
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Open tasks.txt file and read the task data
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    # Filter out empty lines
    task_data = [t for t in task_data if t != ""]

# Initialize an empty list for tasks
task_list = []
for t_str in task_data:
    # Split the task components by semicolon and store them in a dictionary
    curr_t = {}
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    # Append the task to the task list
    task_list.append(curr_t)

# Login Section
'''This code reads usernames and password from the user.txt file to 
allow a user to login.
'''
# Check if user.txt file exists, if not, create it with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert the user data to a dictionary where each key is a username and each value is the corresponding password
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

print("\n")

# Initialize a flag to track whether the user is logged in
logged_in = False

# Keep asking for a username and password until the user logs in successfully
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    
    # If the username does not exist in the username_password dictionary,
    # print an error message and continue with the next iteration of the loop
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    
    # If the entered password does not match the stored password for the
    # entered username, print an error message and continue with the next iteration of the loop
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    
    # If the entered username and password are correct, print a success message and set the logged_in flag to True
    else:
        print("Login Successful!")
        logged_in = True


while True:
    print()
    # Present the menu to the user and convert the user input to lower case
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
mt - Manage Tasks
gr - Generate Reports
ds - Display statistics
e - Exit
: ''').lower()

    # Call the appropriate function based on the user's selection
    if menu == 'r':
        reg_user(username_password)
        
    elif menu == 'a':
        add_task(task_list, username_password, date, datetime, DATETIME_STRING_FORMAT)

    elif menu == 'va':
        view_all(curr_user, task_list, DATETIME_STRING_FORMAT)

    elif menu == 'vm':
        view_mine(curr_user, task_list, DATETIME_STRING_FORMAT)

    elif menu == 'mt':
        manage_task(task_list, datetime, DATETIME_STRING_FORMAT)

    elif menu == "gr":
        generate_task_report(task_list,date)
        generate_user_report(task_list, username_password, date)
        print("Text files generated! Please check local folder!")

    # If the user is an admin they can display statistics about the number of
    # users and tasks.
    elif menu == 'ds' and curr_user == 'admin': 
        print("-----------------------------------")
        print("Generated task report: \n")          #Newline for readability

        # Call the display_task_report function
        display_task_report(os, generate_task_report)

        print("-----------------------------------")
        print("Generated user report: \n")          #Newline for readability