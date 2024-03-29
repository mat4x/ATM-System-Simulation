from tkinter import Label, Button
from PIL import ImageTk, Image
import config
       

def transaction_ended_window(transaction_status):
	config.Window.clear_screen(config.screen)
	config.EN_NUMPAD = False
	config.CAN_TERMINATE = False
	config.CARD_REMOVE = True
	config.TIMER = False

	info = ".\\images\\info.gif" if config.PLATFORM == "Windows" else "./images/info.gif"
	global INFO_IMG, RECEIPT
	INFO_IMG = ImageTk.PhotoImage(Image.open(info).resize((50,50), Image.ANTIALIAS))
	Label(config.screen, image=INFO_IMG, bg=config.DARK_BLUE).place(relx=0.025, rely=0.3, anchor='w')


	if transaction_status == "CANCELLED":
		Label(config.screen, text="Transaction Terminated", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "SUCCESS":
		config.Data_Access.save_acc(config.CURR_USER_ACC)
		Label(config.screen, text="Transaction Successful", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "FAILURE":
		Label(config.screen, text="Transaction Failed", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')

	elif transaction_status == "UNREADABLE":
		Label(config.screen, text="Card Not Readable", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "BLOCKED":
		Label(config.screen, text="Card usage has been\nBLOCKED", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "INCORRECT_PIN":
		Label(config.screen, text="Incorrect PIN Entered", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "TIMED OUT":
		Label(config.screen, text="Time Limit Exceeded", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')

	elif transaction_status == "INVALID_AMOUNT":
		Label(config.screen, text="Invalid Denomination", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "WITHDRAW_LIMIT":
		Label(config.screen, text="Enter Lesser Amount", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')	
	elif transaction_status == "INSUFFICIENT_BAL":
		Label(config.screen, text="Insufficient Balance", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "INVALID_ACCOUNT":
		Label(config.screen, text="Invalid Account Entered", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "NO_CASH":
		Label(config.screen, text="Unavailable.\nPlease try again later", fg='white', bg=config.DARK_BLUE, font=(None, 30),justify='left').place(relx=0.15, rely=0.3, anchor='w')

	elif transaction_status == "PIN_NOT_MATCH":
		Label(config.screen, text="Confirm PIN\nDoesn't Match", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "SAME_PIN_ENTERED":
		Label(config.screen, text="Please Enter\na Different PIN", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "PIN_CHANGED_SUCCESSFULLY":
		config.Data_Access.save_acc(config.CURR_USER_ACC)
		Label(config.screen, text="Your PIN has\nbeen Updated", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')

	else:
		print("None error at Messages")


	if config.PRINT_RECEIPT:
		ratio = config.win.winfo_height()/config.win.winfo_width()
		receipt = ".\\images\\receipt.png" if config.PLATFORM == "Windows" else "./images/receipt.png"
		RECEIPT = ImageTk.PhotoImage(Image.open(receipt).resize((100,100), Image.ANTIALIAS))
		recpt = Button(config.win, image=RECEIPT, bg=config.BLUE, border=0, command = lambda: recpt.destroy())
		config.win.after(2000, lambda: recpt.place(relx=ratio+((1-ratio)/2)-0.04, rely=0.83, anchor='n'))

	Label(config.screen, text="Please take your card", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.5, rely=0.7, anchor='center')
	
	config.PRINT_RECEIPT = False
	config.screen.after(5000, lambda: config.Advert_Cycle.advert_window(config.screen))


def ATM_unavailable():
	info = ".\\images\\info.gif" if config.PLATFORM == "Windows" else "./images/info.gif"
	global INFO_IMG
	INFO_IMG = ImageTk.PhotoImage(Image.open(info).resize((50,50), Image.ANTIALIAS))
	Label(config.screen, image=INFO_IMG, bg=config.DARK_BLUE).place(relx=0.025, rely=0.3, anchor='w')

	Label(config.screen, text="ATM Unavailable\nat the Moment", fg='white',justify='left', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')



if __name__ == "__main__":
	config.win = config.Window.create_window()
	config.screen = config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)

	config.PRINT_RECEIPT = True
	transaction_ended_window("FAILURE")

	config.win.mainloop()
