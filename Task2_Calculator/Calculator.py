import tkinter as tk
from tkinter import messagebox

# ---------------- Functions ---------------- #

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Please select an operation!")
            return

        result_label.config(text=str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    operation_var.set("")
    result_label.config(text="0")


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#EAF6F6")

# ---------------- Title ---------------- #

title = tk.Label(
    root,
    text="🧮 Simple Calculator",
    font=("Arial", 22, "bold"),
    bg="#EAF6F6",
    fg="#0F4C75"
)
title.pack(pady=15)

# ---------------- First Number ---------------- #

tk.Label(
    root,
    text="Enter First Number",
    font=("Arial", 12, "bold"),
    bg="#EAF6F6"
).pack(pady=(10, 0))

entry_num1 = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=20
)
entry_num1.pack(pady=5)

# ---------------- Second Number ---------------- #

tk.Label(
    root,
    text="Enter Second Number",
    font=("Arial", 12, "bold"),
    bg="#EAF6F6"
).pack(pady=(10, 0))

entry_num2 = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=20
)
entry_num2.pack(pady=5)

# ---------------- Operation Selection ---------------- #

tk.Label(
    root,
    text="Select Operation",
    font=("Arial", 12, "bold"),
    bg="#EAF6F6"
).pack(pady=(15, 5))

operation_var = tk.StringVar()

operation_frame = tk.Frame(root, bg="#EAF6F6")
operation_frame.pack()

tk.Radiobutton(
    operation_frame,
    text="+ Add",
    variable=operation_var,
    value="+",
    font=("Arial", 11),
    bg="#EAF6F6"
).grid(row=0, column=0, padx=10)

tk.Radiobutton(
    operation_frame,
    text="- Subtract",
    variable=operation_var,
    value="-",
    font=("Arial", 11),
    bg="#EAF6F6"
).grid(row=0, column=1, padx=10)

tk.Radiobutton(
    operation_frame,
    text="× Multiply",
    variable=operation_var,
    value="*",
    font=("Arial", 11),
    bg="#EAF6F6"
).grid(row=1, column=0, padx=10, pady=5)

tk.Radiobutton(
    operation_frame,
    text="÷ Divide",
    variable=operation_var,
    value="/",
    font=("Arial", 11),
    bg="#EAF6F6"
).grid(row=1, column=1, padx=10, pady=5)

# ---------------- Buttons ---------------- #

button_frame = tk.Frame(root, bg="#EAF6F6")
button_frame.pack(pady=20)

calculate_btn = tk.Button(
    button_frame,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="#3282B8",
    fg="white",
    width=12,
    cursor="hand2",
    command=calculate
)
calculate_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#E74C3C",
    fg="white",
    width=12,
    cursor="hand2",
    command=clear
)
clear_btn.grid(row=0, column=1, padx=10)

# ---------------- Result Section ---------------- #

result_frame = tk.Frame(root, bg="#EAF6F6")
result_frame.pack(pady=20)

tk.Label(
    result_frame,
    text="RESULT",
    font=("Arial", 13, "bold"),
    bg="#EAF6F6",
    fg="#0F4C75"
).pack()

result_label = tk.Label(
    result_frame,
    text="0",
    font=("Arial", 24, "bold"),
    width=15,
    height=2,
    bg="white",
    fg="#27AE60",
    relief="solid",
    bd=2
)
result_label.pack(pady=8)

# ---------------- Footer ---------------- #

footer = tk.Label(
    root,
    text="Basic Arithmetic Calculator",
    font=("Arial", 10),
    bg="#EAF6F6",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
