import tkinter as tk
from tkinter import messagebox


def get_number(object):
    num = object.get()
    try:
        v = float(num)
    except ValueError:
        return None
    return v


def evaluate():
    x = get_number(en_1)
    if x is None:
        messagebox.showerror("Error", "Invalid argument in the first field.")
        en_1.focus_set()
        return
    y = get_number(en_2)
    if y is None:
        messagebox.showerror("Error", "Invalid argument in the second field.")
        en_2.focus_set()
        return
    op = option.get()
    if op == 3 and y == 0:
        messagebox.showerror("Error", "Cannot divide by zero.")
        en_2.focus_set()
        return
    if op == 0:
        result = x + y
    elif op == 1:
        result = x - y
    elif op == 2:
        result = x * y
    else:
        result = x / y
    messagebox.showinfo("Result", str(result))

window = tk.Tk()
window.title("Calculator")
en_1 = tk.Entry(window)
en_2 = tk.Entry(window)
option = tk.IntVar()
add = tk.Radiobutton(window, text="+", variable=option, value=0)
sub = tk.Radiobutton(window, text="-", variable=option, value=1)
mult = tk.Radiobutton(window, text="*", variable=option, value=2)
div = tk.Radiobutton(window, text="/", variable=option, value=3)
button = tk.Button(window, text="Evaluate", command=evaluate)

en_1.grid(row=0, rowspan=4, column=0)
en_1.focus_set()
add.grid(row=0, column=1)
sub.grid(row=1, column=1)
mult.grid(row=2, column=1)
div.grid(row=3, column=1)
en_2.grid(row=0, rowspan=4, column = 2)
button.grid(row=4, columnspan=3)
window.mainloop()