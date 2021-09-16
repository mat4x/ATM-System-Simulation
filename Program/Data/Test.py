from tkinter import Tk, PhotoImage, Label
win=Tk()
img=PhotoImage(file='Card.gif')
Label(win,image=img).pack()
win["bg"] = "#0000ff"
win.geometry("500x500")
win.mainloop()
