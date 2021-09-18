from tkinter import Tk, Label, Button, Entry, BOTH, X, Y, PhotoImage
import config


def read_amount():
	amount = int(config.ENTRY_BOX.get())
	if amount > 100000:
		print("limit 1 lac")

	elif not(amount%50==0):
		print("Invalid denomination")

	elif amount > config.CURR_USER_ACC.balance:
		print("Insufficient Balance")
		
	else:
		print("Okay")


def withdraw_screen():
	config.Window.clear_screen(config.screen)
	config.EN_NUMPAD = True
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
    config.CURR_USER_ACC = config.Classes.Account(103010, "Personal", "Amar Patel",  50000, 203021, 2110)

    withdraw_screen()

    config.win.mainloop()