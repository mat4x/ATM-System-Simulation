import pandas as pd

class IncorrectPIN(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class AccountUnavailable(Exception):
    pass


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
        return [card_status, attempts]

    def attempt(self):
        self.attempts+=1

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
    '''c1 = Card("Ananya",632457,"Available",0)
    if input("Block[B] or Free[F]").lower() == 'b': c1.block()
    else: c1.free()'''

    c1 = Account(1000, "Personal",    "Mayur",   "Sharma",  700001,  400701,  1001)
    c2 = Account(5050, "Personal",    "Priyanshi",   "Singhal", 100000,  512468,  2020)



    
    
