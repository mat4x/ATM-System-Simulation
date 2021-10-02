from tkinter import *
import config
from Classes import Account

def transfer(c1, c2,e):
    amount = int(e.get())
    if c1.balance >= amount:
        c1.balance -=amount
        c2.balance += amount
        config.Message_Windows.transaction_ended_window("SUCCESS")
    else:
        print("Insufficient balance")
        config.Message_Windows.transaction_ended_window("FAILURE")

    print(c1.balance, c2.balance)


def fund_transfer_screen(win):
    config.EN_NUMPAD = True
    Label(win, text="Enter Account number",bg=config.DARK_BLUE, fg="white", font=(None, 25)).place(relx=0.5, rely=0.3, anchor='center')

    e = Entry(win)
    e.place(relx=0.5, rely=0.4, anchor='center')
    config.ENTRY_BOX = e
    config.NEXT_WINDOW = lambda: fund_transfer_screen_2(win) 

def fund_transfer_screen_2(win):
    config.Window.clear_screen(win)

    Label(win, text="Enter amount", bg=config.DARK_BLUE, fg="white", font=(None, 50)).place(relx=0.5, rely=0.3, anchor='center')

    e = Entry(win)
    e.place(relx=0.5, rely=0.4, anchor='center')
    config.ENTRY_BOX = e
    config.NEXT_WINDOW = lambda: transfer(c1,c2,e)     



if __name__ == "__main__":
    c1 = Account(1234, "Personal", "Mayur", "Sharma", 50000, 70362019460, 2003)
    c2 = Account(5678, "Buiseness", "Priyanshi", "Singhal", 100000, 70362019466, 2003)
    
    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)

    fund_transfer_screen(config.screen)

    config.win.mainloop()
