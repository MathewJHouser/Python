import tkinter as tk
import random

def newxy(xy):
    new = random.randint(1, 440)
    while abs(xy - new) < 50:
        new = random.randint(1, 440)
    return new


def move(event):
    global x, y
    x = newxy(x)
    y = newxy(y)
    button.place(x=x, y=y)


window = tk.Tk()
window.geometry("500x500")
window.title("Catch me!")
button = tk.Button(window, text="Catch me!")
button.bind("<Enter>", move)
x = y = 10
button.place(x=x, y=y)
random.seed()
window.mainloop()