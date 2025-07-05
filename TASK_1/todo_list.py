import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks_gui.json"

class todolist:
    def __init__(self, root):
        self.root = root
        self.root.title("TASK 1 : TODO LIST ")
        self.tasks = self.load_tasks()

        # Input frame
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_input = tk.Entry(self.frame, width=30)
        self.task_input.pack(side=tk.LEFT, padx=5)

        self.priority_var = tk.StringVar(value="Medium")
        self.priority_menu = tk.OptionMenu(self.frame, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.pack(side=tk.LEFT)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        # Task listbox
        self.lstbox = tk.lstbox(root, width=60, selectmode=tk.SINGLE)
        self.lstbox.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.complete_btn = tk.Button(btn_frame, text="Mark Complete", command=self.mark_complete)
        self.complete_btn.grid(row=0, column=0, padx=5)

        self.update_btn = tk.Button(btn_frame, text="Update Task", command=self.update_task)
        self.update_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Delete Task", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        self.populate_tasks()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_tasks(self):
     if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Warning: Corrupted or empty tasks file. Starting fresh.")
                return []
     return []


    def save_tasks(self):
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def populate_tasks(self):
        self.lstbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "✓" if task["done"] else " "
            text = f"[{status}] {task['title']} ({task['priority']})"
            self.lstbox.insert(tk.END, text)

            # Color coding
            if task["done"]:
                self.lstbox.itemconfig(idx, fg="gray")
            elif task["priority"] == "High":
                self.lstbox.itemconfig(idx, fg="red")
            elif task["priority"] == "Medium":
                self.lstbox.itemconfig(idx, fg="orange")
            elif task["priority"] == "Low":
                self.lstbox.itemconfig(idx, fg="green")

    def add_task(self):
        title = self.task_input.get().strip()
        priority = self.priority_var.get()
        if title:
            self.tasks.append({"title": title, "done": False, "priority": priority})
            self.task_input.delete(0, tk.END)
            self.populate_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task title.")

    def mark_complete(self):
        selected = self.lstbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = True
            self.populate_tasks()
        else:
            messagebox.showinfo("Selection Error", "Please select a task to mark as complete.")

    def delete_task(self):
        selected = self.lstbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.populate_tasks()
        else:
            messagebox.showinfo("Selection Error", "Please select a task to delete.")

    def update_task(self):
        selected = self.lstbox.curselection()
        if selected:
            index = selected[0]
            current_task = self.tasks[index]

            # Get new title and priority
            new_title = self.task_input.get().strip()
            new_priority = self.priority_var.get()

            if new_title:
                current_task["title"] = new_title
                current_task["priority"] = new_priority
                self.populate_tasks()
                self.task_input.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task title.")
        else:
            messagebox.showinfo("Selection Error", "Please select a task to update.")

    def on_close(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = todolist(root)
    root.mainloop()