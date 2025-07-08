import tkinter as tk
from tkinter import messagebox

import json
import os
TASKS_FILE="tasks_gui.json"
class todolist:
    def __init__(self, root):
        self.root= root
        self.root.title("todo List ")
        self.tasks=self.load_tasks()

         # this is the input frame 
        self.frame =tk.Frame(root)
        self.frame.pack(pady=10)
        self.task_input = tk.Entry(self.frame,width=30)
        self.task_input.pack(side=tk.LEFT, padx=5)

        self.pri=tk.StringVar(value="Medium")
        self.pr_menu= tk.OptionMenu(self.frame,self.pri, "Low","Medium",  "High")
        self.pr_menu.pack(side =tk.LEFT)
        self.add_b= tk.Button(self.frame,text="Add Task", command=self.add_task)

        self.add_b.pack(  side =tk.LEFT,padx=5)

         #Task listbox
        self.lstbox =tk.Listbox(root, width=60,selectmode=tk.SINGLE)
        self.lstbox.pack(pady=10)

        # Buttons
        btn_frame =tk.Frame(root)
        btn_frame.pack()

        self.c_btn = tk.Button(btn_frame, text="Mark Complete", command=self.mark_complete)
        self.c_btn.grid(row=0, column=0, padx=5)
        self.modify_btn= tk.Button(btn_frame, text="Update Task", command=self.update_task)
        self.modify_btn.grid(row=0, column=1, padx=5)

        self.deletion=tk.Button (btn_frame, text="Delete Task", command=self.delete_task)
        self.deletion.grid(row=0,column=2, padx=5)
        self.imp()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_tasks(self):
     if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Warning: Corrupted or empty tasks file. starting fresh")
                return []
     return []


    def saving(self):
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks,file, indent=4 )

    def imp(self):
        self.lstbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "✓" if task["done"] else " "
            text =f"[{status}]  {task['title']}({task['priority']})"
            self.lstbox.insert(tk.END, text)

                     ## this is to deciding Color 
            if task["done"]:
                self.lstbox.itemconfig(idx,fg="gray")
            elif task["priority"]=="High":
                self.lstbox.itemconfig (idx, fg="red")
            elif task["priority"] =="Medium":
                self.lstbox.itemconfig ( idx,  fg="orange")
            elif task["priority"] == "Low":
                self.lstbox.itemconfig(idx,fg="green")

    def add_task(self):
        title= self.task_input.get().strip()
        priority=self.pri.get()
        if title:
            self.tasks.append({"title": title, "done": False, "priority": priority})
            self.task_input.delete(0, tk.END)
            self.imp()
        else:
            messagebox.showwarning("Input Error","please enter a task title.")

    def mark_complete(self):
        selected=self.lstbox.curselection()
        if selected:
            index= selected[0]
            self.tasks[index]["done"] =True
            self.imp()
        else:
            messagebox.showinfo("Selection Error","Please select a task to mark as complete.")

    def delete_task(self):
        selected =self.lstbox.curselection()
        if selected:
            index =selected[0]
            del self.tasks[index]
            self.imp()
        else:
            messagebox.showinfo (  "Selection Error", "Please select a task to delete.")

    def update_task(self):
        selected =self.lstbox.curselection()
        if selected:
            index=selected[0]
            current_task =self.tasks[index]

            # Getting the new title and the priority
            new_title= self.task_input.get().strip()
            new_priority=self.pri.get()

            if new_title:
                current_task["title"]= new_title
                current_task["priority"] = new_priority
                self.imp()
                self.task_input.delete ( 0, tk.END)
            else:
                messagebox.showwarning( "input Error", "Please enter a new task title.")
        else:
            messagebox.showinfo("selection Error","Please select a task to update.")

    def on_close(self):
        self.saving()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app =todolist(root)
    root.mainloop()