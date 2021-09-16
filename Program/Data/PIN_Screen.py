from tkinter import Tk,Button, Entry, Label
import config


def card_authenticate():

	#if matchs pass
		enter_pin_screen()

def enter_pin_screen():
	config.Window.clear_screen(config.screen)
	Label(config.screen, text="PIN SCREEN", font=(None,50)).place(relx=0.5, rely=0.5, anchor='center')


if __name__ == "__main__":

	config.win = config.Window.create_window()
	config.screen= config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)

	card_authenticate()

	config.USER_ACC = config.Classes.Account(103010, "Personal", "Amar Patel",  200200, 203021, 2110)

	config.win.mainloop()
