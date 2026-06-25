import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_NAME = "tasks.json"

# ---------------- Load Tasks ----------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# ---------------- Save Tasks ----------------
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# ---------------- Refresh List ----------------
def refresh_tasks():
    task_list.delete(*task_list.get_children())

    for index, task in enumerate(tasks):
        task_list.insert(
            "",
            "end",
            values=(
                index + 1,
                task["title"],
                task["priority"],
                task["status"]
            )
        )

    update_progress()

# ---------------- Add Task ----------------
def add_task():
    title = task_entry.get().strip()
    priority = priority_var.get()

    if title == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    tasks.append({
        "title": title,
        "priority": priority,
        "status": "Pending"
    })

    save_tasks()
    refresh_tasks()

    task_entry.delete(0, tk.END)

# ---------------- Delete Task ----------------
def delete_task():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    index = task_list.index(selected[0])

    tasks.pop(index)

    save_tasks()
    refresh_tasks()

# ---------------- Complete Task ----------------
def complete_task():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    index = task_list.index(selected[0])

    tasks[index]["status"] = "Completed"

    save_tasks()
    refresh_tasks()

# ---------------- Update Task ----------------
def update_task():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    title = task_entry.get().strip()

    if title == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    index = task_list.index(selected[0])

    tasks[index]["title"] = title
    tasks[index]["priority"] = priority_var.get()

    save_tasks()
    refresh_tasks()

    task_entry.delete(0, tk.END)
    priority_var.set("Medium")

# ---------------- Load Selected Task ----------------
def load_selected_task(event):
    selected = task_list.selection()

    if selected:
        index = task_list.index(selected[0])

        task_entry.delete(0, tk.END)
        task_entry.insert(0, tasks[index]["title"])

        priority_var.set(tasks[index]["priority"])

# ---------------- Update Progress ----------------
def update_progress():
    total = len(tasks)

    if total == 0:
        progress["value"] = 0
        percentage_label.config(text="0% Completed")
        return

    completed = sum(
        1 for task in tasks
        if task["status"] == "Completed"
    )

    percent = (completed / total) * 100

    progress["value"] = percent
    percentage_label.config(
        text=f"{percent:.0f}% Completed"
    )

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Smart To-Do Manager")
root.geometry("900x600")
root.configure(bg="#1E1E1E")

tasks = load_tasks()

# ---------------- Title ----------------
title = tk.Label(
    root,
    text="SMART TO-DO MANAGER",
    font=("Arial", 22, "bold"),
    bg="#1E1E1E",
    fg="cyan"
)
title.pack(pady=15)

# ---------------- Input Frame ----------------
input_frame = tk.Frame(root, bg="#1E1E1E")
input_frame.pack(pady=10)

task_entry = tk.Entry(
    input_frame,
    width=40,
    font=("Arial", 12)
)
task_entry.grid(row=0, column=0, padx=10)

priority_var = tk.StringVar()
priority_var.set("Medium")

priority_menu = ttk.Combobox(
    input_frame,
    textvariable=priority_var,
    values=["High", "Medium", "Low"],
    width=10,
    state="readonly"
)
priority_menu.grid(row=0, column=1)

add_btn = tk.Button(
    input_frame,
    text="Add Task",
    bg="green",
    fg="white",
    command=add_task
)
add_btn.grid(row=0, column=2, padx=10)

# ---------------- Task Table ----------------
columns = ("ID", "Task", "Priority", "Status")

task_list = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

for col in columns:
    task_list.heading(col, text=col)

task_list.column("ID", width=50)
task_list.column("Task", width=450)
task_list.column("Priority", width=120)
task_list.column("Status", width=120)

task_list.pack(pady=20)

# ---------------- Buttons ----------------
btn_frame = tk.Frame(root, bg="#1E1E1E")
btn_frame.pack()

complete_btn = tk.Button(
    btn_frame,
    text="Mark Completed",
    bg="blue",
    fg="white",
    command=complete_task
)
complete_btn.grid(row=0, column=0, padx=10)

update_btn = tk.Button(
    btn_frame,
    text="Update Task",
    bg="orange",
    fg="white",
    command=update_task
)
update_btn.grid(row=0, column=1, padx=10)

delete_btn = tk.Button(
    btn_frame,
    text="Delete Task",
    bg="red",
    fg="white",
    command=delete_task
)
delete_btn.grid(row=0, column=2, padx=10)

# ---------------- Progress Section ----------------
progress_label = tk.Label(
    root,
    text="Task Completion",
    font=("Arial", 12),
    bg="#1E1E1E",
    fg="white"
)
progress_label.pack(pady=10)

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=400,
    mode="determinate"
)
progress.pack()

percentage_label = tk.Label(
    root,
    text="0% Completed",
    font=("Arial", 12),
    bg="#1E1E1E",
    fg="cyan"
)
percentage_label.pack(pady=10)

refresh_tasks()

# ---------------- Bind Selection ----------------
task_list.bind("<<TreeviewSelect>>", load_selected_task)

root.mainloop()
