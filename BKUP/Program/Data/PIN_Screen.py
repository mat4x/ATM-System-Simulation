from tkinter import Tk,Button, Entry, Label
import config

def start_timeout(disp, time=0):
	T_Limit = 20

	try: disp['text'] = str(T_Limit-time)
	except: pass

	if time==T_Limit and config.TIMER:
		config.Message_Windows.transaction_ended_window("TIMED OUT")
	elif config.TIMER:
		config.win.after( 1000, lambda: start_timeout(disp, time+1) )
	else:		####
		print("Timer Stopped")


def validate_pin():
	config.TIMER = False
	try: entered_PIN = config.ENTRY_BOX.get()
	except: entered_PIN = 'INVALID'
	if  entered_PIN == config.CURR_USER_ACC.card_PIN:
		print("Correct PIN: Access Account")
		config.Select_Options_Window.select_transaction_screen()
	else:
		config.CURR_CARD.attempt()
		config.Message_Windows.transaction_ended_window("INCORRECT_PIN")

def enter_pin_screen():
	config.TEXT_LIMIT = 4
	config.CAN_TERMINATE = True
	config.Window.clear_screen(config.screen)
	config.EN_NUMPAD = True
	config.TIMER = True

	time = Label(config.screen, text='0', font=(None,50) ,bg=config.DARK_BLUE, fg='white')
	time.place(relx=0.8, rely=0.1, anchor='center')
	start_timeout(time)

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

	config.CURR_CARD = config.Classes.Card("Amar Patel", 200200)
	config.CURR_USER_ACC = config.Classes.Account(103010, "Personal", "Amar", "Patel",  200200, 203021, 2110)

	enter_pin_screen()

	config.win.mainloop()
