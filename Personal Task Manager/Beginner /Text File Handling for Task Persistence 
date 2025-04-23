from datetime import datetime

# File name to store tasks
file_name = "tasks.txt"

# Function to load tasks from the file
def load_tasks_from_file():
    tasks = []
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):  # Process tasks in 4 lines
                if i + 3 < len(lines):
                    tasks.append({
                        "name": lines[i].strip(),
                        "description": lines[i + 1].strip(),
                        "priority": lines[i + 2].strip(),
                        "due_date": lines[i + 3].strip()
                    })
    except FileNotFoundError:
        print("The file tasks is not found. Starting with an empty task list.")
    except:
        print("Error loading tasks.")
    return tasks

# Function to save tasks to the file
def save_tasks_to_file(tasks):
    try:
        with open(file_name, "w") as file:
            for task in tasks:
                file.write(f"{task['name']}\n{task['description']}\n{task['priority']}\n{task['due_date']}\n")
    except:
        print("Error saving tasks.")

# Function to add a task
def add_task(tasks):
    while True:
        try:
            name = input("Enter task name: ")
            description = input("Enter task description (To leave blank, put '-'): ")
            priority = input("Enter task priority (High/Medium/Low): ").capitalize()
            due_date = input("Enter due date (DD-MM-YYYY): ")

            if priority not in ["High", "Medium", "Low"]:
                print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
                continue

            try:
                datetime.strptime(due_date, "%d-%m-%Y")
            except ValueError:
                print("Incorrect date format, please use DD-MM-YYYY.")
                continue

            confirm = input("Are you sure you want to add this task? (yes/no): ").strip().lower()
            if confirm == "yes":
                tasks.append({"name": name, "description": description, "priority": priority, "due_date": due_date})
                print("Task added successfully.")
                save_tasks_to_file(tasks)
                break
            else:
                print("Task addition cancelled.")
                break
        except:
            print("An unexpected error occurred. Please try again.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        count = 1
        for task in tasks:
            print(f"\n{count}. \nName: {task['name']} \nDescription: {task['description']} \nPriority: {task['priority']} \nDue Date: {task['due_date']}")
            count += 1

# Function to update a task
def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to update: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task index. Try again.")
            return

        name = input("Enter new name OR leave blank to keep current: ")
        description = input("Enter new description OR leave blank to keep current: ")
        priority = input("Enter new priority (High/Medium/Low) OR leave blank to keep current: ")
        due_date = input("Enter new due date (DD-MM-YYYY) OR leave blank to keep current: ")

        if priority and priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Update cancelled.")
            return

        if due_date:
            try:
                datetime.strptime(due_date, "%d-%m-%Y")
            except ValueError:
                print("Invalid date format. Update cancelled.")
                return

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
            save_tasks_to_file(tasks)
        else:
            print("Task update cancelled.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except:
        print("An unexpected error occurred. Please try again.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task index. Try again.")
            return

        confirm = input("Are you sure you want to delete this task? (yes/no): ").strip().lower()
        if confirm == "yes":
            deleted_task = tasks.pop(index)
            print(f"Task '{deleted_task['name']}' deleted successfully.")
            save_tasks_to_file(tasks)
        else:
            print("Task deletion cancelled.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except:
        print("An unexpected error occurred. Please try again.")

# Function to display menu
def menu():
    tasks = load_tasks_from_file()
    while True:
        print("\nTask Manager Menu:")
        print("  1. Add Task")
        print("  2. View Tasks")
        print("  3. Update Task")
        print("  4. Delete Task")
        print("  5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# calling the main code
if __name__ == "__main__":
    menu()
