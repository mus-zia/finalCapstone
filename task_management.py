'''This is file 2/3 of the task manager program, and should be placed in the
 same directory as:
                - task_manager.py (MAIN FILE)
                - report_management.py
                - task_management.py (THIS FILE)'''

# ===================== Define login functions =====================
# Functions called in the login menu are defined in the login_functions.py 
# file in this directory

'''Since moving the functions from the main task_manager.py file into 
this separate file, it is now necessary to pass in the dependent
variables as arguments into the functions we defined.
This ensure when they are called from the main file, the correct
arguments are passed in and no errors occur.'''

# REG_USER FUNCTION: This function allows a user to register a new account.
def reg_user(username_password):                                  
    '''Add a new user to the user.txt file'''
    # Request input of a new username
    new_username = input("New Username: ")
    
    # If the username already exists in the username_password dictionary, print an error message and return from the function
    if new_username in username_password.keys():        
        print(f"User:{new_username} already exists!")   
        print("\Please try again or select another option below!") 
        return                                          

    # Request input of a new password
    new_password = input("New Password: ")

    # Request input of password confirmation
    confirm_password = input("Confirm Password: ")

    # Check if the new password and confirmed password are the same
    if new_password == confirm_password:
        # If they are the same, add them to the user.txt file
        print("New user added")
        username_password[new_username] = new_password
        
        # Write the updated username_password dictionary back to user.txt
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # If the new password and confirmed password are not the same, print an error message
    else:
        print("Passwords do not match")


# ADD_TASK_FUNCTION: This function allows a user to add a new task.
def add_task(task_list, username_password, date, datetime, DATETIME_STRING_FORMAT): 
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    # Ask the user for the username of the person assigned to the task
    task_username = input("Name of person assigned to task: ")
    
    # If the username does not exist in the username_password dictionary, print an error message and return from the function
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return 

    # Ask the user for the title of the task
    task_title = input("Title of Task: ")
    
    # Ask the user for the description of the task
    task_description = input("Description of Task: ")
    
    # Ask the user for the due date of the task until a valid date is entered
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Get the current date
    curr_date = date.today()
    
    # Create a new task dictionary with the entered information and set the 'completed' field to False
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Append the new task to the task list
    task_list.append(new_task)
    
    # Write the updated task list back to tasks.txt
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    
    # Print a success message
    print("Task successfully added.")


# VIEW_ALL FUNCTION: This function allows an admin user to view all tasks.
def view_all(curr_user, task_list, DATETIME_STRING_FORMAT):       
    '''Reads the task from task.txt file and prints to the console in the 
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling) 
    '''
    # Check if the current user is an admin
    if curr_user == 'admin':                    
        # Loop over all tasks, providing a unique identifier for each task
        for task_counter, t in enumerate(task_list, start=1):
            # Build a string to display the task details
            disp_str = f"Unique Task Ref Number: {task_counter}\n" 
            disp_str += f"Completion: {task_list[task_counter-1]['completed']}\n" 
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            # Print the task details
            print(disp_str)
    else:
        # If the current user is not an admin, print an error message
        print(f"{curr_user} does not have admin privileges!!")


# VIEW_MINE FUNCTION: This function allows a user to view their tasks.
def view_mine(curr_user, task_list, DATETIME_STRING_FORMAT):      
    '''Reads the task from task.txt file and prints to the console in the 
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling)
    '''

    # Enumerate provides a counter for all the tasks, not just the user's tasks.
    # This provides a unique identifier for each task, regardless of which user
    # it belongs to. This allows for collaboration across users.
    for task_counter, t in enumerate(task_list, start=1): 
        # Only process tasks belonging to the current user
        if t['username'] == curr_user:
            # Build a string to display the task details
            disp_str = f"Unique Task Ref Number (UTR): {task_counter}\n" 
            disp_str += f"Completion: {task_list[task_counter-1]['completed']}\n" 
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            # Print the task details
            print(disp_str)


# MANAGE_TASK FUNCTION: This function manages user tasks, allowing the user to 
#                       mark tasks as complete or edit tasks
def manage_task(task_list, datetime, DATETIME_STRING_FORMAT):     
   '''Allows the user to select a specific task and perform actions on it'''
   # Ask the user to enter the Unique Task Reference (UTR) number of the task they want to manage
   selected_task = int(input("Enter the Unique Task Reference (UTR) number of the task you want to manage or '-1' to return to the main menu: "))
   
   # If the user wants to return to the main menu, return from the function
   if selected_task == -1:
       return
   
   # If the selected task number is invalid, print an error message and return from the function
   elif selected_task > len(task_list) or selected_task <= 0:
       print("Invalid task number. Please try again.")
       return
   
   # Otherwise, adjust the selected task number for zero-indexing and proceed with the task management
   else:
       selected_task -= 1 
       # If the task is already completed, print a message and return from the function
       if task_list[selected_task]['completed']:
           print("This task has already been marked as complete.")
           return
       
       # Ask the user what action they want to perform on the task
       action = input("What would you like to do with this task? Enter 'c' to mark as complete or 'e' to edit: ")
       
       # If the user wants to mark the task as complete, do so and print a confirmation message
       if action.lower() == 'c':
           task_list[selected_task]['completed'] = True
           print("Task marked as complete.")
       
       # If the user wants to edit the task, ask them for the new username and due date (if provided), update the task accordingly, and print a confirmation message
       elif action.lower() == 'e':
           new_username = input("Enter the new username for the task or press enter to keep the current username: ")
           if new_username:
               task_list[selected_task]['username'] = new_username
           new_due_date = input("Enter the new due date for the task (YYYY-MM-DD) or press enter to keep the current due date: ")
           if new_due_date:
               task_list[selected_task]['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
           print("Task updated.")
       
       # If the user entered an invalid action, print an error message
       else:
           print("Invalid action. Please try again.")

   # After performing the desired action on the task, write the updated and completed tasks back to tasks.txt
   with open("tasks.txt", "w") as task_file:
       task_list_to_write = []
       for t in task_list:
           # Format the task attributes as strings, join them with semicolons, and append the resulting string to task_list_to_write
           str_attrs = [
              t['username'],
              t['title'],
              t['description'],
              t['due_date'].strftime(DATETIME_STRING_FORMAT),
              t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
              "Yes" if t['completed'] else "No"
           ]
           task_list_to_write.append(";".join(str_attrs))
       # Join the strings in task_list_to_write with newline characters and write the resulting string to tasks.txt
       task_file.write("\n".join(task_list_to_write))


#===================== Generate (Task and User) Reports Functions =====================
           
# GENERATE_TASK_REPORT FUNCTION: This function generates a task report.
def generate_task_report(task_list,date):
    # Calculate the total number of tasks
    total_tasks = len(task_list)
    
    # Count the number of completed tasks
    completed_tasks = sum(t['completed'] for t in task_list)
    
    # Calculate the number of uncompleted tasks
    uncompleted_tasks = total_tasks - completed_tasks
    
    # Count the number of overdue tasks
    overdue_tasks = sum((not t['completed']) and t['due_date'].date() < date.today() for t in task_list)
    
    # Calculate the percentage of completed tasks
    completion_percentage = round((completed_tasks / total_tasks) * 100,2) if total_tasks > 0 else 0
    
    # Calculate the percentage of overdue tasks
    overdue_percentage = round((overdue_tasks / total_tasks) * 100,2) if total_tasks > 0 else 0

    # Open the file "task_overview.txt" in write mode
    with open("task_overview.txt", "w") as report_file:
        # Write the total number of tasks, completed tasks, uncompleted tasks, overdue tasks, 
        # completion percentage, and overdue percentage to the report file
        report_file.write(f"Total tasks: {total_tasks}\n")
        report_file.write(f"Completed tasks: {completed_tasks}\n")
        report_file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        report_file.write(f"Overdue tasks: {overdue_tasks}\n")
        report_file.write(f"Completion percentage: {completion_percentage}%\n")
        report_file.write(f"Overdue percentage: {overdue_percentage}%\n")

# GENERATE_USER_REPORT FUNCTION: This function generates a user report.
def generate_user_report(task_list, username_password, date):
    # Calculate the total number of users and tasks
    total_users = len(username_password.keys())
    total_tasks = len(task_list)

    # Initialize an empty dictionary to hold user statistics
    user_stats = {}

    # Iterate over each task in the task list
    for t in task_list:
        # If the username is not already in user_stats, initialize its entry
        if t['username'] not in user_stats:
            user_stats[t['username']] = {'total_tasks': 0, 'completed_tasks': 0, 'overdue_tasks': 0}
        # Increment the total_tasks count for the user
        user_stats[t['username']]['total_tasks'] += 1
        # If the task is completed, increment the completed_tasks count for the user
        if t['completed']:
            user_stats[t['username']]['completed_tasks'] += 1
        # If the task is not completed and is due today, increment the overdue_tasks count for the user
        if not t['completed'] and t['due_date'].date() < date.today():
            user_stats[t['username']]['overdue_tasks'] += 1

    # Open the file "user_overview.txt" in write mode
    with open("user_overview.txt", "w") as report_file:
        # Write the total number of users and tasks to the report file
        report_file.write(f"Total users: {total_users}\n")
        report_file.write(f"Total tasks: {total_tasks}\n")

        # Iterate over each user and their statistics
        for user, stats in user_stats.items():
            # Extract the total tasks, completed tasks, and overdue tasks for the user
            total_user_tasks = stats['total_tasks']
            completed_user_tasks = stats['completed_tasks']
            overdue_user_tasks = stats['overdue_tasks']

            # Calculate the percentage of total tasks, completed tasks, remaining tasks, and overdue tasks for the user
            task_percentage = round((total_user_tasks / total_tasks) * 100,2) if total_tasks > 0 else 0
            completion_percentage = round((completed_user_tasks / total_user_tasks) * 100,2) if total_user_tasks > 0 else 0
            remaining_percentage = round(((total_user_tasks - completed_user_tasks) / total_user_tasks) * 100,2) if total_user_tasks > 0 else 0
            overdue_percentage = round((overdue_user_tasks / total_user_tasks) * 100,2) if total_user_tasks > 0 else 0

            # Write the user's statistics to the report file
            report_file.write(f"\nUser: {user}\n")
            report_file.write(f"Tasks assigned: {total_user_tasks}\n")
            report_file.write(f"Percentage of total tasks: {task_percentage}%\n")
            report_file.write(f"Completed tasks: {completed_user_tasks}\n")
            report_file.write(f"Percentage of completed tasks: {completion_percentage}%\n")
            report_file.write(f"Remaining tasks: {total_user_tasks - completed_user_tasks}\n")
            report_file.write(f"Percentage of remaining tasks: {remaining_percentage}%\n")
            report_file.write(f"Overdue tasks: {overdue_user_tasks}\n")
            report_file.write(f"Percentage of overdue tasks: {overdue_percentage}%\n")

