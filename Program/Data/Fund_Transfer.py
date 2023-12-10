from tkinter import *
import config
from Classes import Account

def transfer(e):
    config.PRINT_RECEIPT = True

    amount = int(e.get())
    print(amount)
    if config.CURR_USER_ACC.balance >= amount:
        config.CURR_USER_ACC.balance -= amount
        config.RECEIVER_ACC.balance += amount
        config.Data_Access.save_acc(config.CURR_USER_ACC)
        config.Data_Access.save_acc(config.RECEIVER_ACC)
        config.Message_Windows.transaction_ended_window("SUCCESS")
    else:
        print("Insufficient balance")
        config.Message_Windows.transaction_ended_window("INSUFFICIENT_BAL")


def valid_acc(account):
    config.RECEIVER_ACC = config.Data_Access.get_acc(account)
    if config.RECEIVER_ACC == None or config.RECEIVER_ACC.acc_no == config.CURR_USER_ACC.acc_no:
        config.Message_Windows.transaction_ended_window("INVALID_ACCOUNT")
    else:
        fund_transfer_screen_2()
        
        
    
def fund_transfer_screen():
    win = config.screen
    config.TEXT_LIMIT = 10
    config.Window.clear_screen(win)
    config.EN_NUMPAD = True
    Label(win, text="Enter Account Number",bg=config.DARK_BLUE, fg="white", font=(None, 33)).place(relx=0.5, rely=0.35, anchor='center',)

    e = Entry(win,font=(None,50), justify="center")
    e.place(relx=0.5, rely=0.7, anchor='center', height=80, width=400)
    config.ENTRY_BOX = e
    config.NEXT_WINDOW = lambda: valid_acc(int(e.get())) 

def fund_transfer_screen_2():
    win= config.screen
    config.Window.clear_screen(win)

    Label(win, text="Enter Amount", bg=config.DARK_BLUE, fg="white", font=(None, 50)).place(relx=0.5, rely=0.35, anchor='center')

    amount_entry = Entry(win, font=(None,50), justify= "center")
    amount_entry.place(relx=0.5, rely=0.7, anchor='center', height=80, width=400)
    config.ENTRY_BOX = amount_entry
    config.NEXT_WINDOW = lambda: transfer(amount_entry)



if __name__ == "__main__":
   
    config.CURR_USER_ACC = config.Data_Access.get_acc(5050)
    
    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)

    fund_transfer_screen()

    config.win.mainloop()
