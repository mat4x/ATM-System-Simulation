from tkinter import Tk, Button, Label, HORIZONTAL
from tkinter.ttk import Progressbar
import config


def paste_message(message):
	print(message)
	Label(config.screen, text=message, fg="white", bg=config.DARK_BLUE,
		font=(None,20)).place(relx=0.5, rely=0.7, anchor='center')


def progress_loading(bar, message):
	val = bar['value']
	bar['value'] =(val+4)
	print(bar['value'])
	
	if bar['value'] >= 100: paste_message(message)
	else: bar.after(100, lambda: progress_loading(bar, message))
	

def loading_screen(message):
	config.Window.clear_screen(config.screen)
	Label(config.screen, text="Please Wait", fg="white", bg=config.DARK_BLUE,
		font=(None,40)).place(relx=0.5, rely=0.3, anchor='center')
	bar = Progressbar(config.screen, orient = HORIZONTAL,
              length = 300, mode = 'determinate')
	bar.place(relx=0.5, rely=0.5, anchor='center')
	bar.after(0, lambda: progress_loading(bar, message))


if __name__ == "__main__":
	config.win = config.Window.create_window()
	config.screen = config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)

	loading_screen("Done")

	config.win.mainloop()