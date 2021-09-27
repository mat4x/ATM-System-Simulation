from tkinter import Label
from PIL import ImageTk, Image
import config
       

def transaction_ended_window(transaction_status):
	config.Window.clear_screen(config.screen)
	config.EN_NUMPAD = False
	config.CAN_TERMINATE = False
	config.CARD_REMOVE = True

	info = ".\\images\\info.gif"
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
	
	elif transaction_status == "INVALID_AMOUNT":
		Label(config.screen, text="Invalid Denomination", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "WITHDRAW_LIMIT":
		Label(config.screen, text="Enter Lesser Amount", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')	
	elif transaction_status == "INSUFFICIENT_BAL":
		Label(config.screen, text="Insufficient Balance", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	
	#invalid account number
	#confirmation pin does not match
	
	else:
		print("Yo, we got an error")


	Label(config.screen, text="Please take your card", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.5, rely=0.7, anchor='center')
	
	config.screen.after(5000, lambda: config.Advert_Cycle.advert_window(config.screen))


if __name__ == "__main__":
	config.win = config.Window.create_window()
	config.screen = config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)

	transaction_ended_window("FAILURE")

	config.win.mainloop()
