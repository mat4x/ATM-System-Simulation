from tkinter import Tk, Entry, Button, Label, StringVar

def greet(win, name):
    Label(win, text=f"Hello {name}").grid(row=2, column=0, columnspan=2)

win = Tk()
Label(win, text="Enter Name:").grid(row=0, column=0)

entry = Entry(win)
entry.grid(row=0, column=1)

Button(win, text="Submit", command=lambda: greet(win,entry.get())).grid(row=1, column=0)

win.mainloop()
