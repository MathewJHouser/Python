import tkinter as tk
from tkinter import messagebox
from random import randrange


wnd = tk.Tk()
wnd.title("TicTacToe")


def set_ox(btn, sign):
    btn["fg"] = btn["activeforeground"] = "red" if sign == 'X' else "green"
    btn["text"] = sign


def winner():
    for sign in ("X", "O"):
        for x in range(3):
            if sign == board[x][0]["text"] == board[x][1]["text"] == board[x][2]["text"]:
                return sign
            if sign == board[0][x]["text"] == board[1][x]["text"] == board[2][x]["text"]:
                return sign
        if sign == board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]:
            return sign
        if sign == board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]:
            return sign
    return None


def free_cells():
    list = []
    for row in range(3):
        for col in range(3):
            if board[row][col]["text"] == "":
                list.append( (row, col) )
    return list


def announce(win):
    messagebox.showinfo("Game Over!", ("I" if win == "X" else "You") + " won!")
    wnd.destroy()
    exit(0)

def clicked(event):
    btn = event.widget
    if btn["text"] != "":
        return
    set_ox(btn, "O")
    if not winner() is None:
        announce("O")
    free = free_cells()
    this = free[randrange(0, len(free))]
    set_ox(board[this[0]][this[1]], "X")
    if not winner() is None:
        announce("X")


board = [[None for c in range(3)] for r in range(3)]
for col in range(3):
    for row in range(3):
        btn = tk.Button(wnd, width=4, height=1, font=("Arial", 30, "bold"), text="")
        btn.bind("<Button-1>", clicked)
        btn.grid(column=col, row=row)
        board[row][col] = btn
set_ox(board[1][1], "X")
wnd.mainloop()