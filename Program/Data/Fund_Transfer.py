from tkinter import *
import config
from Classes import Account

def transfer(c1, c2,e):
    amount = int(e.get())
    if c1.balance >= amount:  
        c1.balance -=amount
        c2.balance += amount
        config.Message_Windows.transaction_ended_window("SUCCESS")
        # Save data into file
    else:
        print("Insufficient balance")
        config.Message_Windows.transaction_ended_window("INSUFFICIENT_BAL")

    c1.details()
    c2.details()


def valid_acc(account):
    config.RECEIVER_ACC = config.Data_Access.get_acc(account)
    if config.RECEIVER_ACC == None or config.RECEIVER_ACC.acc_no == config.CURR_USER_ACC.acc_no:
        config.Message_Windows.transaction_ended_window("INVALID_ACCOUNT")
    else:
        fund_transfer_screen_2()
        
        
    
def fund_transfer_screen():
    win = config.screen
    config.TEXT_LIMIT = 6
    config.Window.clear_screen(win)
    config.EN_NUMPAD = True
    Label(win, text="Enter Account number",bg=config.DARK_BLUE, fg="white", font=(None, 25)).place(relx=0.5, rely=0.35, anchor='center',)

    e = Entry(win,font=(None,50), justify="center")
    e.place(relx=0.5, rely=0.7, anchor='center', height=80, width=400)
    config.ENTRY_BOX = e
    config.NEXT_WINDOW = lambda: valid_acc(int(e.get())) 

def fund_transfer_screen_2():
    win= config.screen
    config.Window.clear_screen(win)

    Label(win, text="Enter amount", bg=config.DARK_BLUE, fg="white", font=(None, 50)).place(relx=0.5, rely=0.35, anchor='center')

    e = Entry(win, font=(None,50), justify= "center")
    e.place(relx=0.5, rely=0.7, anchor='center', height=80, width=400)
    config.ENTRY_BOX = e
    config.NEXT_WINDOW = lambda: transfer(config.CURR_USER_ACC, config.RECEIVER_ACC ,e)     



if __name__ == "__main__":
    c1 = Account(5678, "Buiseness", "Priyanshi", "Singhal", 100000, 70362019466, 2003)
    
    config.CURR_USER_ACC = c1
    
    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)

    fund_transfer_screen()

    config.win.mainloop()
