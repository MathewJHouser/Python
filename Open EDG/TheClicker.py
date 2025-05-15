import tkinter as tk
from random import randint

def tick():
    global clock_value, after_id
    if clock_started:
        clock_value += 1
        clock_label["text"] = str(clock_value)
        after_id = clock_label.after(1000, tick)

def button_clicked(event):
    global clock_started
    if not clock_started:
        clock_started = True
        clock_label.after(1000, tick)
    clicked_button = event.widget
    clicked_value = int(clicked_button["text"])
    if clicked_value == numbers[0]:
        clicked_button["state"] = tk.DISABLED
        del numbers[0]
    if len(numbers) == 0:
        clock_started=False
        clock_label.after_cancel(after_id)

window = tk.Tk()
window.title("Clicker")
numbers = []
for i in range(25):
    new_num = randint(1, 999)
    while new_num in numbers:
        new_num = randint(1, 999)
    numbers.append(new_num)
for i in range(25):
    new_button = tk.Button(window, text=str(numbers[i]), width=10)
    new_button.grid(column=i//5, row=i % 5)
    new_button.bind("<Button-1>", button_clicked)

numbers.sort()
clock_value = 0
clock_label = tk.Label(window, text=str(clock_value))
clock_label.grid(column=2, row=5)
clock_started=False
window.mainloop()



