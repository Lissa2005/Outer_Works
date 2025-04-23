import os
import json
from datetime import datetime

#JSON file name
file_name = "tasks.json"

# List of dictionaries for tasks
tasks = []

# Functions for CRUD operations
#function to add tasks
def add_task():
    try:
        name = input("Enter task name: ")
        description = input("Enter descripton (or '-' to skip): ")
        priority = input("Enter priority (High/Medium/Low): ").capitalize()
        due_date = input("Enter due date (DD-MM-YYYY)(eg: 30-04-2024): ")

        if priority not in ["High","Medium","Low"]:
            print("Invaild priority. Please enter High,Medium, or Low.")
            return

        try:
            datetime.strptime(due_date, "%d-%m-%Y")
        except ValueError:
            print("Invaild date formate. Please use DD-MM-YYYY.")
            return

        confirm =input("Are you sure you want to add this task? (yes/no): ").lower()
        if confirm == "yes":
            task = {
                "Name": name,
                "Description": description,
                "Priority": priority,
                "Due date": due_date
            }
            tasks.append(task)
            save_tasks_to_json()
            print("Task added successfully.")
        else:
            print("Task addition cancelled.")

    except Exception as e:
        print(f"Error adding task: {e}")


#function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        i = 1
        for task in tasks:
            print(f"\n{i}. Name: {task['Name']}")
            print(f"   Description: {task['Description']}")
            print(f"   Priority: {task['Priority']}")
            print(f"   Due Date: {task['Due date']}")
            i += 1

#function to update a task
def update_task():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter task number to update: "))-1
        if index < 0 or index>= len(tasks):
            print("Invaild task number.")
            return

        task = tasks[index]
        name = input(f"New name(leave blank to keep '{task['Name']}'): ") or task['Name']
        description = input(f"New description (leave blank to keep current): ") or task['Description']
        priority = input("New priority (High/Medium/Low or leave blank to keep current): ").capitalize() or task['Priority']
        due_date = input("New due date (DD-MM-YYYY or leave blank to keep current): ") or task['Due date']

        if priority not in ["High","Medium","Low"]:
            print("Invaild priority. Update Cancelled.")
            return

        try:
            datetime.strptime(due_date, "%d-%m-%Y")
        except ValueError:
            print("Invaild date format. Update cancelled,")
            return

        confirm = input("Are you sure you want to update this task? (yeas/no): ").lower()
        if confirm == "yes":
            tasks[index] = {
                "Name": name,
                "Description": description,
                "Priority": priority,
                "Due date": due_date
                }
            save_tasks_to_json()
            print("Task update successfully.")
        else:
            print("Update cancelled.")

    except ValueError:
        print("Please enter a vaild number.")
    except Exception as e:
        print(f"Error updating task: {e}")

#function to delete a task
def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: "))-1
        if index < 0 or index >= len(tasks):
            print("Invaild task number")
            return

        confirm = input("Are you sure you want to delete this task? (yea/no): ").lower()
        if confirm == "yes":
            removed = tasks.pop(index)
            save_tasks_to_json()
            print(f"Task '{removed['Name']}' Deleted successfully.")
        else:
            print("Deletion cancelled")

    except ValueError:
        print("Please enter a vaild number.")
    except Exception as e:
        print(f"Error deleting task:{e}")
        

# JSON file handling functions
#function to load tasks from json file
def load_tasks_from_json():
    try:
        with open(file_name, "r") as file:
            return json.load(file)  # Return the loaded list
    except FileNotFoundError:
        print("No JSON file found. Starting with empty task list.")
        return []  # Return an empty list if file not found
    except json.JSONDecodeError:
        print("JSON file is corrupt. Starting fresh.")
        return []  # Return an empty list if JSON is invalid

def save_tasks_to_json():
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")



# Main function
if __name__ == "__main__":
    # Load existing tasks from JSON into global `tasks` list
    tasks = load_tasks_from_json()  

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()  
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    
