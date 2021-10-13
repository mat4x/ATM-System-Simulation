from tkinter import Label
from PIL import ImageTk, Image
import config
       

def transaction_ended_window(transaction_status):
	config.Window.clear_screen(config.screen)
	config.EN_NUMPAD = False
	config.CAN_TERMINATE = False
	config.CARD_REMOVE = True
	config.TIMER = False

	info = ".\\images\\info.gif" if config.PLATFORM == "Windows" else "./images/info.gif"
	global INFO_IMG
	INFO_IMG = ImageTk.PhotoImage(Image.open(info).resize((50,50), Image.ANTIALIAS))
	Label(config.screen, image=INFO_IMG, bg=config.DARK_BLUE).place(relx=0.025, rely=0.3, anchor='w')


	if transaction_status == "CANCELLED":
		Label(config.screen, text="Transaction Terminated", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "SUCCESS":
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
		Label(config.screen, text="Confirm PIN doesn't match", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "SAME_PIN_ENTERED":
		Label(config.screen, text="Please Enter\na different PIN", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "PIN_CHANGED_SUCCESSFULLY":
		Label(config.screen, text="Your PIN has\nbeen updated", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')

	else:
		print("Yo, we got an error at Messages")

	Label(config.screen, text="Please take your card", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.5, rely=0.7, anchor='center')
	
	config.screen.after(10000, lambda: config.Advert_Cycle.advert_window(config.screen))


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

	transaction_ended_window("FAILURE")

	config.win.mainloop()
