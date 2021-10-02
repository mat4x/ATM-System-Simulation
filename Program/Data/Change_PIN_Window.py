from tkinter import *
from Classes import Account
import config


def change_PIN():
    config.CURR_USER_ACC.details()
    config.EN_NUMPAD = True
    config.CAN_TERMINATE = True
    config.TEXT_LIMIT = 4

    config.Window.clear_screen(config.screen)
    gui1 = config.screen
    Label(gui1, text="New PIN", font=(None, 40), bg=config.DARK_BLUE, fg='white').place(relx=0.5 ,rely=0.5, anchor='center')

    config.ENTRY_BOX = Entry(gui1, font=(None,50), justify='center')
    config.ENTRY_BOX.place(relx=0.5 ,rely=0.7, anchor='center', height=80, width=400)
    
    config.NEXT_WINDOW = check_with_existing_PIN

def check_with_existing_PIN():
    config.CURR_USER_ACC.details()
    if int(config.ENTRY_BOX.get()) == config.CURR_USER_ACC.card_PIN:
        config.Message_Windows.transaction_ended_window("SAME_PIN_ENTERED")
    else:
        confirm_new_PIN()

def confirm_new_PIN():
    config.TEXT_LIMIT = 4
    config.CH_PINS[0] = config.ENTRY_BOX.get()
    config.Window.clear_screen(config.screen)
    gui2 = config.screen
    Label(gui2, text="Confirm New PIN: ", font=(None, 40), bg=config.DARK_BLUE, fg='white').place(relx=0.5 ,rely=0.5, anchor='center')

    config.ENTRY_BOX = Entry(gui2, font=(None,50), justify='center')
    config.ENTRY_BOX.place(relx=0.5 ,rely=0.7, anchor='center', height=80, width=400)

    config.NEXT_WINDOW = check

def check():
    config.CH_PINS[1] = config.ENTRY_BOX.get()

    if config.CH_PINS[0] == config.CH_PINS[1]:
        print("PIN changed successfully")
        
        config.CURR_CARD.card_PIN = config.CH_PINS[0]
        print(config.CURR_CARD.card_PIN)
        config.Message_Windows.transaction_ended_window("PIN_CHANGED_SUCCESSFULLY")
    else:
        config.Message_Windows.transaction_ended_window("PIN_NOT_MATCH")

if __name__ == "__main__":
    
    config.win = config.Window.create_window()					#window is already created
    config.screen = config.Window.create_screen(config.win)		#create widgets(Label/Button/Entry) in this screen variable in function
    config.Window.create_numpad(config.win, config.screen)


    config.CURR_USER_ACC = config.Classes.Account(103010, "Personal", "Amar", "Patel",  200200, 203021, 2110)	#sample user account/ use this variable to test program
    config.CURR_CARD = config.Classes.Card("Amar Patel", 200200)
    config.CURR_USER_ACC.details()
    change_PIN()
    config.win.mainloop()
    
    #check(change_PIN(), c1.card_PIN)
    
