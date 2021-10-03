from tkinter import Tk, Label, Button, Entry, BOTH, X, Y, PhotoImage
from PIL import Image, ImageTk
import config


def collect_cash(cash):
	[child.destroy() for child in cash]


def dispense_cash(amount):
	ratio = config.win.winfo_height()/config.win.winfo_width()
	notes500 = amount//500
	notes100 = (amount-notes500*500)//100
	disp = min(7, notes100+notes500)

	global IMG100, IMG500
	IMG100 = ".\\images\\Note_100.gif" if config.PLATFORM=="Windows" else "./images/Note_100.gif"
	IMG500 = ".\\images\\Note_500.gif" if config.PLATFORM=="Windows" else "./images/Note_500.gif"
	IMG100 = ImageTk.PhotoImage(Image.open(IMG100).resize((200,93), Image.ANTIALIAS))
	IMG500 = ImageTk.PhotoImage(Image.open(IMG500).resize((200,93), Image.ANTIALIAS))

	cash = []
	for i in range(disp-1):
		note_img = IMG500 if i<notes500 else IMG100
		cash.append( Label(config.win, image=note_img, bg=config.BLUE, border=0) )
		cash[i].place(relx=ratio+((1-ratio)/2), rely=0.7, y=(disp-i)*5, anchor='n')

	cash.append( Button(config.win, image=IMG500 if notes500>=disp else IMG100, bg=config.BLUE, border=0, command= lambda: collect_cash(cash)) )
	cash[disp-1].place(relx=ratio+((1-ratio)/2), rely=0.7, anchor='n')


def read_amount():
	config.EN_NUMPAD = False
	config.CAN_TERMINATE = False
	try: amount = int(config.ENTRY_BOX.get())
	except: amount = 0

	if amount > 25000:
		print("limit Rs. 25000")
		config.Message_Windows.transaction_ended_window("WITHDRAW_LIMIT")

	elif not(amount%100==0) or amount==0:
		print("Invalid denomination")
		config.Message_Windows.transaction_ended_window("INVALID_AMOUNT")

	elif amount > config.CURR_USER_ACC.balance:
		print("Insufficient Balance")
		config.Message_Windows.transaction_ended_window("INSUFFICIENT_BAL")
		
	else:	#All okay
		config.Loading_Screen.loading_screen("Please collect your cash")
		config.win.after(5000, lambda: dispense_cash(amount))
		config.win.after(8500, lambda: config.Message_Windows.transaction_ended_window("SUCCESS"))
		print("Please collect Cash")


def withdraw_screen():
	config.Window.clear_screen(config.screen)
	config.EN_NUMPAD  = True
	config.CAN_TERMINATE =  True
	config.TEXT_LIMIT = 6

	Label(config.screen, text="Enter Amount", bg=config.DARK_BLUE, fg='white', font=(None, 50)).place(relx=0.5,rely=0.35, anchor='center')
	amount_entry = Entry(config.screen, font=(None, 60), justify='center', insertontime=0)		#, show='*'`
	amount_entry.place(relx=0.5,rely=0.7, anchor='center', height=80, width=400)
	amount_entry.focus_set()

	config.ENTRY_BOX = amount_entry
	config.NEXT_WINDOW = read_amount


if __name__ == "__main__":
    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)
    config.CURR_USER_ACC = config.Classes.Account(103010, "Personal", "Amar", "Patel",  10000, 203021, 2110)

    withdraw_screen()

    config.win.mainloop()