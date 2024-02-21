'''This is file 3/3 of the task manager program, and should be placed in the
 same directory as:
                - task_manager.py (MAIN FILE)
                - report_management.py (THIS FILE)
                - task_management.py '''

#===================== Display (Task and User) Report Functions =====================
#===================== used with display statistics "ds" option =====================

'''Since moving the functions from the main task_manager.py file into 
this separate file, it is now necessary to pass in the dependent
variables as arguments into the functions we defined.
This ensure when they are called from the main file, the correct
arguments are passed in and no errors occur.'''

# This function displays a task report.
def display_task_report(os, generate_task_report):
    # Check if the file "task_overview.txt" exists.
    if not os.path.exists("task_overview.txt"):
        # If it doesn't exist, generate the task report.
        generate_task_report()
    # Open the file "task_overview.txt" in read mode.
    with open("task_overview.txt", 'r') as report_file:
        # Print the contents of the file.
        print(report_file.read())

# This function displays a user report.
def display_user_report(os, generate_user_report):
    # Check if the file "user_overview.txt" exists.
    if not os.path.exists("user_overview.txt"):
        # If it doesn't exist, generate the user report.
        generate_user_report()
    # Open the file "user_overview.txt" in read mode.
    with open("user_overview.txt", 'r') as report_file:
        # Print the contents of the file.
        print(report_file.read())
