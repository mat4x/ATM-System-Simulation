from tkinter import Label
import config


def display_acc_details(win):
    name = acc.name
    acc_no = acc.acc_no
    balance = acc.balance
    acc_type = acc.acc_type
    Label(win,text="Account Details",font=(None,30),bg=config.DARK_BLUE,fg="white").place(relx=0.5,rely=0.2,anchor="center")

    Label(win,text="Account Holder Name: ",bg=config.DARK_BLUE,fg="white").place(relx=0.2,rely=0.3)
    Label(win,text="Account Number: ",bg=config.DARK_BLUE,fg="white").place(relx=0.2,rely=0.4)
    Label(win,text="Balance: ",bg=config.DARK_BLUE,fg="white").place(relx=0.2,rely=0.5)
    Label(win,text="Account Type: ",bg=config.DARK_BLUE,fg="white").place(relx=0.2,rely=0.6)

    Label(win,text=name,bg=config.DARK_BLUE,fg="white").place(relx=0.6,rely=0.3)
    Label(win,text=acc_no,bg=config.DARK_BLUE,fg="white").place(relx=0.6,rely=0.4)
    Label(win,text=balance,bg=config.DARK_BLUE,fg="white").place(relx=0.6,rely=0.5)
    Label(win,text=acc_type,bg=config.DARK_BLUE,fg="white").place(relx=0.6,rely=0.6)

    win.after(15000,lambda:print("Transaction Successful"))


if __name__ == "__main__":
    acc = config.Classes.Account(24329,"savings","ananya","mishra",125000,1276283,1243)
    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)

    display_acc_details(config.screen)

    config.win.mainloop()
