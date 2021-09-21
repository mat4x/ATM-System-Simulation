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
        else: print("Insufficient Balance")

    
class Card:
    def __init__(self, name, card_no, card_status="Available", attempts=0):
        self.name        = name
        self.card_no     = card_no
        self.card_status = card_status
        self.attempts    = attempts

    def attempt(self):
        self.attempts+=1

    def block(self):
        self.card_status = "Blocked"
        print("Customer card usage blocked")

    def free(self):
        self.card_status = "Available"
        self.attempts = 0
        print("Customer card usage freed")


if __name__ == "__main__":
    pass
