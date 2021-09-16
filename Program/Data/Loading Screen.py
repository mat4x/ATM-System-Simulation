from tkinter import Tk, Button, Label, HORIZONTAL
from tkinter.ttk import Progressbar
import config


def progress_loading(bar):
	val = bar['value']
	bar['value'] =(val+1)%100
	print(bar['value'])
	bar.after(100, lambda: progress_loading(bar))

def loading_screen(screen):
	bar = Progressbar(screen, orient = HORIZONTAL,
              length = 300, mode = 'determinate')
	bar.place(relx=0.5, rely=0.2, anchor='center')
	bar.after(0, lambda: progress_loading(bar))


if __name__ == "__main__":
	win = config.Window.create_window()
	screen = config.Window.create_screen(win)
	config.Window.create_numpad(win, screen)

	loading_screen(screen)

	win.mainloop()