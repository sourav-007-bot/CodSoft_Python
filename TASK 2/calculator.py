import tkinter as tk
from tkinter import messagebox
import math
    #My calculation logic for this TASK
def calculate(operation):
    try:
        if operation == '√':
            num = float(entry1.get())
            if num < 0:
                raise ValueError("Cannot take square root of a negative number.")
            result = math.sqrt(num)
            result_label.config(text=f"√{num} = {result:.4f}")
            return

          # if binary operations, get both inputs
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        elif operation == '^':
            result = num1 ** num2
        elif operation == '%':
            if num2 == 0:
                raise ZeroDivisionError("cannot perform modulus with zero.")
            result = num1 % num2
        else:
            raise ValueError("unknown operation.")

        result_label.config(text=f"Result: {result:.4f}")

    except ValueError as ve:
        messagebox.showerror("input Error", str(ve))
    except ZeroDivisionError as ze:
        messagebox.showerror("math error",str(ze))
    except Exception:
        messagebox.showerror("unknown Error", "unexpected error occurred.")

#Setup of GUI 
root = tk.Tk()
root.title("calculator")
root.geometry("360x330")
root.configure(bg="#f0f0f0")


tk.Label(root, text="Number 1:",font=('Arial', 12), bg="#f0f0f0").pack(pady=(10, 0))
entry1 = tk.Entry(root,font=('Arial', 12),width=20)
entry1.pack()

tk.Label(root,text="Number 2 (optional for √):", font=('Arial', 12),bg="#f0f0f0").pack(pady=(10, 0))
entry2 = tk.Entry(root, font=('Arial', 12),width=20)
entry2.pack()

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=20)

button_cfg = {'width': 5, 'font': ('Arial', 12), 'padx': 5, 'pady': 5}

tk.Button(btn_frame,text="+", bg="#d4edda", command=lambda: calculate('+'),  **button_cfg).grid(row=0, column=0)
tk.Button(btn_frame, text="-", bg="#f8d7da", command=lambda: calculate('-'),**button_cfg).grid(row=0, column=1)
tk.Button(btn_frame,text="*", bg="#fff3cd",command=lambda: calculate('*'), **button_cfg).grid(row=0, column=2)
tk.Button(btn_frame, text="/",   bg="#d1ecf1", command=lambda: calculate('/'), **button_cfg).grid(row=0, column=3)

tk.Button( btn_frame, text="^", bg="#e2e3e5", command=lambda: calculate('^'), **button_cfg).grid(row=1, column=0)
tk.Button(btn_frame,text="%", bg="#e2e3e5", command=lambda: calculate('%'), **button_cfg).grid(row=1, column=1)
tk.Button(btn_frame, text="√", bg="#c3e6cb",   command=lambda: calculate('√'), **button_cfg).grid(row=1, column=2)

  #  Result display
result_label = tk.Label(root, text="Result: ", font=('Arial', 14), fg="blue", bg="#f0f0f0")
result_label.pack(pady=20)

root.mainloop()