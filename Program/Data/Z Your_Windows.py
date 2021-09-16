from tkinter import Tk, Label, Button, Entry					#If some error with tkinter, replace with *
import config


def window_name():
	#config.EN_NUMPAD = True									#<-- un_comment if you need to use numpad

	'''Try this example then erase this function content
	You can erase this function ans start writing your code here
	Dont forget to call your function down in main for it to actually execute'''

	#Use the variable if you need to access the widget later (eg. Labels)
	l = Label(config.screen, text="This\nWindow", bg=config.DARK_BLUE, font=(None,50))		
	l.place(relx=0.5, rely=0.5, anchor='center')

	#Use this methond if you don't want to acess it later (eg. EntryBoxes -> e.get())
	Button(config.screen, text="Exit Button", bg=config.DARK_BLUE, font=(None,20), command=exit).place(relx=0.5, rely=0.8, anchor='center')

	#accessing the user details who inserted the card
	print(config.USER_ACC.details())
	print("PIN number:", config.USER_ACC.card_PIN)

	##### Function content ends here ####


if __name__ == "__main__":
	config.win = config.Window.create_window()					#window is already created
	config.screen = config.Window.create_screen(config.win)		#create widgets(Label/Button/Entry) in this screen variable in function
	config.Window.create_numpad(config.win, config.screen)

	config.USER_ACC = config.Classes.Account(103010, "Personal", "Amar Patel",  200200, 203021, 2110)	#sample user account/ use this variable to test program

	window_name()												#<----Call your window function here

	config.win.mainloop()