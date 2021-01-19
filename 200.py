from tkinter import *

win = Tk()
win.geometry("1366x768")
win.title("this is 200")

w = 1366
h = 768
x = w//2
y = h//2

canvas = Canvas(win, width = w, height = h, bg = "#478dad")
canvas.pack()

dot = canvas.create_oval(x,y,x+20,y+20, fill = "#f4ad4a")

def left(event):
    x = -10
    y = 0
    canvas.move(dot,x,y)

def right(event):
    x = 10
    y = 0
    canvas.move(dot,x,y)

def up(event):
    x = 0
    y = -10
    canvas.move(dot,x,y)

def down(event):
    x = 0
    y = 10
    canvas.move(dot,x,y)

win.bind("<Left>",left)
win.bind("<Right>",right)
win.bind("<Up>",up)
win.bind("<Down>",down)

win.mainloop()
