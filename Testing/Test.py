from tkinter import *
win = Tk()
win.geometry("500x500")
win.title("Hello World")
Label(win, text='Works', font = (None,20)).pack()
Label(win, text='New Window', font = (None,20)).pack()

L = ["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "heart", "man",
"mouse",
"pirate",
"plus",
"shuttle",
"sizing",
"spider",
"spraycan",
"star",
"target",
"tcross",
"trek",
"watch"]

for i in L:
    Button(win, text=i, cursor=i).pack(fill=X)

win.mainloop()
