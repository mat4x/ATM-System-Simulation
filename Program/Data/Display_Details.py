from tkinter import *
import config


def display_acc_details():
    config.CAN_TERMINATE = False
    config.Window.clear_screen(config.screen)
    win = config.screen
    font_sz = 18
    left  = 0.09
    right = 0.6
    
    name     = config.CURR_USER_ACC.name
    acc_no   = config.CURR_USER_ACC.acc_no
    balance  = f"Rs.{config.CURR_USER_ACC.balance}"
    acc_type = config.CURR_USER_ACC.acc_type
    
    Label(win,text="Account Details",font=(None,40),bg=config.DARK_BLUE,fg="white").place(relx=0.5,rely=0.2,anchor="center")

    Label(win,text="Account Holder Name ",font=(None,font_sz),bg=config.DARK_BLUE,fg="white").place(relx=left,rely=0.4)
    Label(win,text="Account Number "     ,font=(None,font_sz),bg=config.DARK_BLUE,fg="white").place(relx=left,rely=0.5)
    Label(win,text="Account Balance "    ,font=(None,font_sz),bg=config.DARK_BLUE,fg="white").place(relx=left,rely=0.6)
    Label(win,text="Account Type "       ,font=(None,font_sz),bg=config.DARK_BLUE,fg="white").place(relx=left,rely=0.7)

    Label(win,text=name    ,font=(None,font_sz),bg=config.DARK_BLUE,fg="white").place(relx=right,rely=0.4)
    Label(win,text=acc_no  ,font=(None,font_sz),bg=config.DARK_BLUE,fg="white").place(relx=right,rely=0.5)
    Label(win,text=balance ,font=(None,font_sz),bg=config.DARK_BLUE,fg="white").place(relx=right,rely=0.6)
    Label(win,text=acc_type,font=(None,font_sz),bg=config.DARK_BLUE,fg="white").place(relx=right,rely=0.7)

    config.win.after(15000,lambda:config.Message_Windows.transaction_ended_window("SUCCESS"))


if __name__ == "__main__":
    config.CURR_USER_ACC = config.Classes.Account(24329,"savings","Ananya","Mishra",125000,1276283,1243)
    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)

    display_acc_details()

    config.win.mainloop()
