from tkinter import Tk,Button, Entry, Label
import config


def validate_pin():
	try:
		if int(config.ENTRY_BOX.get()) == config.USER_ACC.card_PIN:
			print("Correct PIN: Access Account")
			config.Select_Options_Window.select_transaction_screen()
		else: print("No match")
	except:
		print("No input given")

def enter_pin_screen():
	config.win.geometry("+200+50")
	config.TEXT_LIMIT = 4
	config.CAN_TERMINATE = True
	config.Window.clear_screen(config.screen)
	config.EN_NUMPAD = True

	Label(config.screen, text="Enter PIN", bg=config.DARK_BLUE, fg='white', font=(None, 50)).place(relx=0.5,rely=0.7, anchor='center')
	pin_entry = Entry(config.screen, font=(None, 60), justify='center', insertontime=0)		#, show='*'`
	pin_entry.place(relx=0.5,rely=0.35, anchor='center', height=80, width=400)
	pin_entry.focus_set()

	config.ENTRY_BOX = pin_entry
	config.NEXT_WINDOW = validate_pin


if __name__ == "__main__":

	config.win = config.Window.create_window()
	config.screen= config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)
	config.USER_ACC = config.Classes.Account(103010, "Personal", "Amar Patel",  200200, 203021, 2110)

	enter_pin_screen()

	config.win.mainloop()
