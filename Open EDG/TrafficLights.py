import tkinter as tk

phases = ((True, False, False),
          (False, True, False),
          (False, False, True))

def draw_light(y, color):
    canvas.create_oval(15, y+5, 105, y+95, outline="black", fill=color, width=3)

def red_light(on):
    draw_light(0, "red" if on else "gray")

def yellow_light(on):
    draw_light(100, "yellow" if on else "gray")

def green_light(on):
    draw_light(200, "green" if on else "gray")

def next_phase():
    global phase
    phase = (phase +1) % len(phases)
    red_light(phases[phase][0])
    yellow_light(phases[phase][1])
    green_light(phases[phase][2])

window = tk.Tk()
window.title("Traffic Lights")
canvas = tk.Canvas(window, width=120, height=300, bg="#555555")
canvas.grid(row=0, column=0)
next_button = tk.Button(window, text="Next", command = next_phase)
next_button.grid(row=1, column=0)
quit_button = tk.Button(window, text="Quit", command=window.destroy)
quit_button.grid(row=2, column=0)
phase = -1
next_phase()
window.mainloop()