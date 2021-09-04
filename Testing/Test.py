from tkinter import *
win = Tk()
win.geometry("500x500")
win.title("Hello World")
Label(win, text='It Works', font = (None,20)).grid(row=0, column=0, columnspan=2)
Label(win, text='New Window', font = (None,20)).grid(row=1, column=0, columnspan=2)

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)

L = ["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "man",
"mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", "star", "target",
"tcross", "trek", "watch"]

k = 2
for i in L:
    Button(win, text=i, cursor=i, height = 2).grid(row=(k//2)*2+1, column=k%2, stick='nsew')
    k+=1

win.mainloop()
