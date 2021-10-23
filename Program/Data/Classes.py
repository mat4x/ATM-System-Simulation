import pandas as pd
import config

class IncorrectPIN(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class AccountUnavailable(Exception):
    pass

class Machine:
    def __init__(self, branch_location, status="online", cash_available=5000000):
        self.branch_location = branch_location
        self.status          = status
        self.cash_available  = cash_available
    
    def deduct(self, amount):
        if amount<=self.cash_available:
            self.cash_available -= amount
            
    def data(self):
        return '\n'.join([self.status, self.branch_location, str(self.cash_available)])
        


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

    
class Card:
    def __init__(self, name, card_no, card_status="Available", attempts=0):
        self.name        = name
        self.card_no     = card_no
        self.card_status = card_status
        self.attempts    = int(attempts)

    def get_vals(self):
        return [self.card_status, self.attempts]

    def attempt(self):
        self.attempts+=1
        if self.attempts == 3:
            self.attempts=0
            self.card_status="Blocked"
        config.Data_Access.save_card(config.CURR_CARD)

    def block(self):
        df = pd.read_csv("Cards_Data_Test.csv", dtype=str)
        df.loc[df['Card No'] == str(self.card_no), "Status"] = "Blocked"
        df.loc[df['Card No'] == str(self.card_no), "Attempts"] = "0"
        df.to_csv("Cards_Data_Test.csv", index=False)
        print("Customer card usage blocked")

    def free(self):
        df = pd.read_csv("Cards_Data_Test.csv", dtype=str)
        df.loc[df['Card No'] == str(self.card_no), "Status"] = "Available"
        df.loc[df['Card No'] == str(self.card_no), "Attempts"] = "0"
        df.to_csv("Cards_Data_Test.csv", index=False)
        print("Customer card usage freed")


if __name__ == "__main__":
    pass
