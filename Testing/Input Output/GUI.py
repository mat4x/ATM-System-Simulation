from tkinter import Tk, Entry, Button, Label        #these are called widgets, that will be placed in the window

def greet(win, name):               #The command the submit button will perform
    Label(win, text=f"Hello {name}").grid(row=2, column=0, columnspan=2)

win = Tk()                          #Creating the window

Label(win, text="Enter Name:").grid(row=0, column=0)

entry = Entry(win)                  #Creating the input box where you type in
entry.grid(row=0, column=1)         #Placing the box in the window

Button(win, text="Submit", command=lambda: greet(win,entry.get())).grid(row=1, column=0)    #Creating the submit button

win.mainloop()                      #For the window to stay open
