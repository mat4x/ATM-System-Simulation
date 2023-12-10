from tkinter import Button, Label
from PIL import ImageTk, Image
import config


def select_transaction_screen():
	config.Window.clear_screen(config.screen)
	config.TIMER = False
	config.EN_NUMPAD = False

	Label(config.screen, text = "Weclome to 'Bank' ATM", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.5, rely=0.2, anchor='center')
	Label(config.screen, text = "Please select a Transaction", fg='white', bg=config.DARK_BLUE, font=(None, 20)).place(relx=0.5, rely=0.4, anchor='center')

	Button(config.screen, text='Account Info',  font=(None,15), command=config.Display_Details.display_acc_details).place(relx=0.25, rely=0.6, anchor='center', relwidth=0.35, relheight=0.1)
	Button(config.screen, text='Withdraw Cash', font=(None,15), command=config.Withdraw_Cash.withdraw_screen).place(relx=0.75, rely=0.6, anchor='center', relwidth=0.35, relheight=0.1)
	Button(config.screen, text='Fund Transfer', font=(None,15), command=config.Fund_Transfer.fund_transfer_screen).place(relx=0.25, rely=0.8, anchor='center', relwidth=0.35, relheight=0.1)
	Button(config.screen, text='Change PIN',    font=(None,15), command = config.Change_PIN_Window.change_PIN).place(relx=0.75, rely=0.8, anchor='center', relwidth=0.35, relheight=0.1)


if __name__ == "__main__":
	config.win = config.Window.create_window()
	config.screen = config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)

	select_transaction_screen()

	config.win.mainloop()


'''
Group members:
- Mayur Sharma
- Priyanshi Singhal
- Ananaya Mishra
- Shubham Kumar
'''
