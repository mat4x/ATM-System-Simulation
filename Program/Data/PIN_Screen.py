from tkinter import Tk,Button, Entry, Label
import config


def card_authenticate():
	pass

def enter_pin_screen():
	pass



if __name__ == "__main__":

	config.win = config.Window.create_window()
	config.screen= config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)

	card_authenticate()

	config.USER_ACC = config.Classes.Account(103010, "Personal", "Amar Patel",  200200, 203021, 2110)

	config.win.mainloop()
