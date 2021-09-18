from tkinter import Label
from PIL import ImageTk, Image
import config


def card_unreadable():
        Label(screen, text="Card Not Readable", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')

def transaction_ended_window(screen, transaction_status):
	config.Window.clear_screen(screen)
	info = ".\\images\\info.gif"
	global INFO_IMG
	INFO_IMG = ImageTk.PhotoImage(Image.open(info).resize((50,50), Image.ANTIALIAS))
	Label(screen, image=INFO_IMG, bg=config.DARK_BLUE).place(relx=0.025, rely=0.3, anchor='w')
	
	if transaction_status == "SUCCESS":
		Label(screen, text="Transaction Successful", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	elif transaction_status == "CANCELLED":
		Label(screen, text="Transaction Terminated", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	else:
		Label(screen, text="Transaction Failed", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.15, rely=0.3, anchor='w')
	
	Label(screen, text="Please take your card", fg='white', bg=config.DARK_BLUE, font=(None, 30)).place(relx=0.5, rely=0.7, anchor='center')

	config.CARD_REMOVE = True
	config.EN_NUMPAD = False
	config.CAN_TERMINATE = False

	screen.after(5000, lambda: config.Advert_Cycle.advert_window(screen))


if __name__ == "__main__":
	config.win = config.Window.create_window()
	config.screen = config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)

	transaction_ended_window(config.screen, "FAILED")

	config.win.mainloop()
