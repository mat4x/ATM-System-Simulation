from tkinter import *
from Classes import Account
import config


def change_PIN():
    config.Window.clear_screen(config.screen)
    gui1 = config.screen
    gui1.title("Change PIN")
    w = Label(gui1, text="New PIN: ")
    w.pack()
    new_pin = Entry(gui1)
    new_pin.pack()
    Button(gui1, text = "Submit", command = change_PIN).pack()
    gui1.mainloop()
    #return new_pin

def confirm_new_PIN():
    config.Window.clear_screen(config.screen)
    gui2 = config.screen
    w1 = Label(gui2, text="Confirm New PIN: ")
    w1.pack()
    con_pin = Entry(gui2)
    con_pin.pack()
    Button(gui2, text = "Submit", command = confirm_new_PIN).pack()
    gui2.mainloop()

def check(n1, n2):
    if n1 == n2:
        gui3 = Tk()
        Label(gui3, text = "PIN Changed Successfully").pack()
        c1.card_PIN = n1
        print(c1.card_PIN)
    else:
        gui4 = Tk()
        Label(gui4, text = "PIN Does not Match").pack()
#Button(gui, text="Submit", command = lambda: check(new_pin.get(), con_pin.get() )  ).pack()
#Button(gui, text="Submit", command = lambda: check(new_pin.get(), con_pin.get() )  ).pack()
#gui.mainloop()

if __name__ == "__main__":
    
    config.win = config.Window.create_window()					#window is already created
    config.screen = config.Window.create_screen(config.win)		#create widgets(Label/Button/Entry) in this screen variable in function
    config.Window.create_numpad(config.win, config.screen)


    config.USER_ACC = config.Classes.Account(103010, "Personal", "Amar Patel",  200200, 203021, 2110)	#sample user account/ use this variable to test program
    change_PIN()
    config.win.mainloop()



    
    
    #check(change_PIN(), c1.card_PIN)
    