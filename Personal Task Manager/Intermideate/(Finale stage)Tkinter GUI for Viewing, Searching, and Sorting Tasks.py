import json
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# ------------ Task Class ------------
class Task:
    def __init__(self, name, description, priority, due_date):
        # Initialize task attributes
        self.name = name
        self.description = description
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        # Convert task object into a dictionary for JSON saving
        return {
            "Name": self.name,
            "Description": self.description,
            "Priority": self.priority,
            "Due date": self.due_date
        }

# ------------ TaskManager Class ------------
class TaskManager:
    def __init__(self, json_file="Tasks.json"):
        # Initialize task manager and load tasks from file
        self.json_file = json_file
        self.tasks = []
        self.load_tasks_from_json()

    def add_task(self, task):
        # Add a task to the list and save to file
        self.tasks.append(task)
        self.save_tasks_to_json()

    def update_task(self, index, updated_task):
        # Replace task at specific index with a new task object
        if 0 <= index < len(self.tasks):
            self.tasks[index] = updated_task
            self.save_tasks_to_json()

    def delete_task(self, index):
        # Remove task from the list by index
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks_to_json()

    def load_tasks_from_json(self):
        # Load tasks from a JSON file
        try:
            with open(self.json_file, "r") as file:
                data = json.load(file)
                self.tasks = []
                for t in data:
                    task = Task(
                        name=t["Name"],
                        description=t["Description"],
                        priority=t["Priority"],
                        due_date=t["Due date"]
                    )
                    self.tasks.append(task)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks_to_json(self):
        # Save tasks to a JSON file
        with open(self.json_file, "w") as file:
            task_dicts = []
            for t in self.tasks:
                task_dicts.append(t.to_dict())
            json.dump(task_dicts, file, indent=4)

    def sort_tasks(self, sort_key="name", reverse=False):  # Added reverse param
        if sort_key == "due_date":
            for i in range(len(self.tasks)):
                for j in range(i + 1, len(self.tasks)):
                    date_i = datetime.strptime(self.tasks[i].due_date, "%d-%m-%Y")
                    date_j = datetime.strptime(self.tasks[j].due_date, "%d-%m-%Y")
                    if (date_i > date_j and not reverse) or (date_i < date_j and reverse):
                        self.tasks[i], self.tasks[j] = self.tasks[j], self.tasks[i]
        else:
            for i in range(len(self.tasks)):
                for j in range(i + 1, len(self.tasks)):
                    val_i = getattr(self.tasks[i], sort_key).lower()
                    val_j = getattr(self.tasks[j], sort_key).lower()
                    if (val_i > val_j and not reverse) or (val_i < val_j and reverse):
                        self.tasks[i], self.tasks[j] = self.tasks[j], self.tasks[i]

    def get_filtered_tasks(self, name_filter="", priority_filter="", due_date_filter=""):
        # Return only tasks matching the filters provided
        filtered = []
        for task in self.tasks:
            match = True
            if name_filter and name_filter.lower() not in task.name.lower():
                match = False
            if priority_filter and priority_filter.lower() != task.priority.lower():
                match = False
            if due_date_filter and due_date_filter != task.due_date:
                match = False
            if match:
                filtered.append(task)
        return filtered

# ------------ TaskManagerGUI Class ------------
class TaskManagerGUI:
    def __init__(self, root):
        # Set up the GUI window and task manager
        self.root = root
        self.root.title("Personal Task Manager")
        self.task_manager = TaskManager()

        # ✅ Added to support toggle sort
        self.sort_reverse = {
            "name": False,
            "description": False,
            "priority": False,
            "due_date": False
        }

        self.setup_gui()
        self.populate_tree(self.task_manager.tasks)

    def setup_gui(self):
        # Title label
        tk.Label(self.root, text="Personal Task Manager", font=("Arial", 16)).grid(row=0, column=1, columnspan=6, pady=10)

        # Sidebar for Add/Update/Delete buttons
        button_sidebar = tk.Frame(self.root)
        button_sidebar.grid(row=2, column=0, rowspan=6, padx=10, pady=10, sticky="ns")
        tk.Button(button_sidebar, text="Add Task", width=15, command=self.add_task).pack(pady=5)
        tk.Button(button_sidebar, text="Update Task", width=15, command=self.update_task).pack(pady=5)
        tk.Button(button_sidebar, text="Delete Task", width=15, command=self.delete_task).pack(pady=5)

        # Filter inputs
        tk.Label(self.root, text="Filter by Name:").grid(row=1, column=1, sticky="w")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=2)

        tk.Label(self.root, text="Priority:").grid(row=1, column=3, sticky="w")
        self.priority_combo = ttk.Combobox(self.root, values=["", "High", "Medium", "Low"])
        self.priority_combo.grid(row=1, column=4)

        tk.Label(self.root, text="Due Date (DD-MM-YYYY):").grid(row=1, column=5, sticky="w")
        self.due_date_entry = tk.Entry(self.root)
        self.due_date_entry.grid(row=1, column=6)

        tk.Button(self.root, text="Filter", command=self.apply_filter).grid(row=1, column=7)

        # Treeview for displaying tasks
        columns = ("Name", "Description", "Priority", "Due date")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        self.tree.heading("Name", text="Name", command=self.sort_by_name)
        self.tree.heading("Description", text="Description", command=self.sort_by_description)
        self.tree.heading("Priority", text="Priority", command=self.sort_by_priority)
        self.tree.heading("Due date", text="Due date", command=self.sort_by_due_date)

        for col in columns:
            self.tree.column(col, anchor="center", width=120)

        self.tree.grid(row=2, column=1, columnspan=7, sticky="nsew")
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(7, weight=1)

        # Input fields for creating/updating tasks
        tk.Label(self.root, text="Task Name:").grid(row=3, column=1)
        self.task_name_entry = tk.Entry(self.root)
        self.task_name_entry.grid(row=3, column=2)

        tk.Label(self.root, text="Description:").grid(row=3, column=4)
        self.task_desc_entry = tk.Entry(self.root)
        self.task_desc_entry.grid(row=3, column=5)

        # for space between rows
        tk.Label().grid(row=4)
        # rest of the inputs
        tk.Label(self.root, text="Priority:").grid(row=5, column=1)
        self.task_priority_combo = ttk.Combobox(self.root, values=["High", "Medium", "Low"])
        self.task_priority_combo.grid(row=5, column=2)

        tk.Label(self.root, text="Due Date (DD-MM-YYYY):").grid(row=5, column=4)
        self.task_due_entry = tk.Entry(self.root)
        self.task_due_entry.grid(row=5, column=5)

        # create space like boarder around and made the pop up look nice
        tk.Label().grid(row=5)
        tk.Label().grid(row=6, column=8)

    def populate_tree(self, task_list):
        # Refresh the Treeview with a list of tasks
        self.tree.delete(*self.tree.get_children())
        for task in task_list:
            self.tree.insert("", tk.END, values=(task.name, task.description, task.priority, task.due_date))

    def apply_filter(self):
        # Get input and apply filters to the task list
        name = self.name_entry.get().strip()
        priority = self.priority_combo.get().strip()
        due_date = self.due_date_entry.get().strip()
        tasks = self.task_manager.get_filtered_tasks(name, priority, due_date)
        self.populate_tree(tasks)

    # Sorting handlers for each column
    def sort_by_name(self):
        self.sort_reverse["name"] = not self.sort_reverse["name"]
        self.task_manager.sort_tasks("name", reverse=self.sort_reverse["name"])
        self.populate_tree(self.task_manager.tasks)

    def sort_by_description(self):
        self.sort_reverse["description"] = not self.sort_reverse["description"]
        self.task_manager.sort_tasks("description", reverse=self.sort_reverse["description"])
        self.populate_tree(self.task_manager.tasks)

    def sort_by_priority(self):
        self.sort_reverse["priority"] = not self.sort_reverse["priority"]
        self.task_manager.sort_tasks("priority", reverse=self.sort_reverse["priority"])
        self.populate_tree(self.task_manager.tasks)

    def sort_by_due_date(self):
        self.sort_reverse["due_date"] = not self.sort_reverse["due_date"]
        self.task_manager.sort_tasks("due_date", reverse=self.sort_reverse["due_date"])
        self.populate_tree(self.task_manager.tasks)

    def add_task(self):
        # Create and add a new task
        name = self.task_name_entry.get().strip()
        description = self.task_desc_entry.get().strip()
        priority = self.task_priority_combo.get().strip()
        due_date = self.task_due_entry.get().strip()

        if not (name and description and priority and due_date):
            print("All fields are required to add a task.")
            return

        new_task = Task(name, description, priority, due_date)
        self.task_manager.add_task(new_task)
        self.populate_tree(self.task_manager.tasks)

    def update_task(self):
        # Update selected task with new data (partial update allowed)
        selected = self.tree.selection()
        if not selected:
            print("Please select a task to update.")
            return
        index = self.tree.index(selected[0])
        current_task = self.task_manager.tasks[index]

        # Get new input, but keep existing value if left blank
        name = self.task_name_entry.get().strip()
        description = self.task_desc_entry.get().strip()
        priority = self.task_priority_combo.get().strip()
        due_date = self.task_due_entry.get().strip()

        if not name:
            name = current_task.name
        if not description:
            description = current_task.description
        if not priority:
            priority = current_task.priority
        if not due_date:
            due_date = current_task.due_date

        updated_task = Task(name, description, priority, due_date)
        self.task_manager.update_task(index, updated_task)
        self.populate_tree(self.task_manager.tasks)

    def delete_task(self):
        # Delete the selected task from the list
        selected = self.tree.selection()
        if not selected:
            print("Please select a task to delete.")
            return

        index = self.tree.index(selected[0])
        self.task_manager.delete_task(index)
        self.populate_tree(self.task_manager.tasks)

# ------------ Main Execution ------------
if __name__ == "__main__":
    root = tk.Tk()  # Create application window
    root.geometry("1100x450")  # Set default window size
    app = TaskManagerGUI(root)  # Launch GUI
    root.mainloop()  # Start event loop
