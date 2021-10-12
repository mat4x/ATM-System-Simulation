from tkinter import *

class Account:
    def __init__(self, acc_no, acc_type, fname, lname, balance, card_no, card_PIN):
        self.acc_no   = acc_no
        self.acc_type = acc_type
        self.fname    = fname
        self.lname    = lname
        self.name     = f"{fname} {lname}"
        self.balance  = balance
        self.card_no  = card_no
        self.card_PIN = card_PIN

    def get_vals(self):
        return [self.balance, self.card_PIN]

    def details(self):
        print("\n------Customer Details-------")
        print("Account Number\t:", self.acc_no)
        print("Account type\t:",   self.acc_type)
        print("Account holder\t:", self.fname, self.lname)
        print("Available Bal\t:",  self.balance)

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance -= amount
            print(f"Rs.{amount} deducted from account")
            config.Data_Access.save_acc(self)
        else: print("Insufficient Balance")

    def transfer(self, reciever, amount):
        self.balance -= amount
        reciever.balance += amount
        config.Data_Access.save_acc(self)
        config.Data_Access.save_acc(reciever)

def display_acc_details(win):
    name = acc.name
    acc_no = acc.acc_no
    balance = acc.balance
    acc_type = acc.acc_type
    Label(win,text="Account Details",font=(None,30),bg="blue",fg="white").place(relx=0.5,rely=0.2,anchor="center")

    Label(win,text="Account Holder Name: ").place(relx=0.2,rely=0.3)
    Label(win,text="Account Number: ").place(relx=0.2,rely=0.4)
    Label(win,text="Balance: ").place(relx=0.2,rely=0.5)
    Label(win,text="Account Type: ").place(relx=0.2,rely=0.6)

    Label(win,text=name).place(relx=0.6,rely=0.3)
    Label(win,text=acc_no).place(relx=0.6,rely=0.4)
    Label(win,text=balance).place(relx=0.6,rely=0.5)
    Label(win,text=acc_type).place(relx=0.6,rely=0.6)

    win.after(15000,lambda:print("Transaction Successful"))


if __name__ == "__main__":
    acc = Account(24329,"savings","ananya","mishra",125000,1276283,1243)
    win =Tk()
    win.geometry("500x500")
    win.configure(bg="yellow")
    display_acc_details(win)

    win.mainloop()
