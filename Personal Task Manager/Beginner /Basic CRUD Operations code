from datetime import datetime

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    while True:
        try:
            # Collect task details from user
            name = input("Enter task name: ")
            description = input("Enter task description (To leave blank, put '-'): ")
            priority = input("Enter task priority (High/Medium/Low): ").capitalize()
            due_date = input("Enter due date (DD-MM-YYYY): ")
            
            # Validate priority and due date
            if priority not in ['High', 'Medium', 'Low']:
                print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
                continue
            
            try:
                # Validate date format
                datetime.strptime(due_date, '%d-%m-%Y')
            except ValueError:
                print("Incorrect date format, please use DD-MM-YYYY.")
                continue
            
            # Validate inputs (no empty fields allowed except description)
            if not name or not priority or not due_date:
                print("All fields are required! Please try again.")
                continue
            
            # Confirm action before adding task
            confirm = input("Are you sure you want to add this task? (yes/no): ").strip().lower()
            if confirm == "yes":
                task = {"name": name, "description": description, "priority": priority, "due_date": due_date}
                tasks.append(task)
                print("Task added successfully.")
                break
            else:
                print("Task addition cancelled.")
                break
        except ValueError:
            print("Invalid input. Please try again.")
        except TypeError:
            print("An unexpected type error occurred. Please try again.")
        except Exception:
            print("An unexpected error occurred. Please try again.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        index = 1  # Initialize index
        for task in tasks:
            print(f"\n{index}. \nName: {task['name']} \nDescription: {task['description']} \nPriority: {task['priority']} \nDue Date: {task['due_date']}\n")
            index += 1  # numbering index manually

# Function to update a task
def update_task():
    view_tasks()
    if not tasks:
        return
    
    while True:
        try:
            # Get task number from user
            index = int(input("Enter task number to update: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task index. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Allow user to update specific fields or leave them unchanged
        name = input("Enter new name OR leave blank to keep current: ")
        description = input("Enter new description OR leave blank to keep current: ")
        priority = input("Enter new priority OR leave blank to keep current: ")
        due_date = input("Enter new due date OR leave blank to keep current: ")
        
        # Confirm before updating the task
        confirm = input("Are you sure you want to update this task? (yes/no): ").strip().lower()
        if confirm == "yes":
            if name:
                tasks[index]["name"] = name
            if description:
                tasks[index]["description"] = description
            if priority:
                tasks[index]["priority"] = priority
            if due_date:
                tasks[index]["due_date"] = due_date
            print("Task updated successfully.")
        else:
            print("Task update cancelled.")
        break

# Function to delete a task
def delete_task():
    view_tasks()
    if not tasks:
        return
    
    while True:
        try:
            # Get task number from user
            index = int(input("Enter task number to delete: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task index. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Confirm before deleting the task
        confirm = input("Are you sure you want to delete this task? (yes/no): ").strip().lower()
        if confirm == "yes":
            tasks.pop(index)
            print("Task deleted successfully.")
        else:
            print("Task deletion cancelled.")
        break

# Function to display menu
def menu():
    while True:
        # Display menu options
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
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# calling main code
if __name__ == "__main__":
    menu()
