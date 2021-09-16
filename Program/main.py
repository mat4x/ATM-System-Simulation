from os import chdir, getcwd
import sys;		sys.path.extend([getcwd()+".\\Data\\", getcwd()+".\\Data\\images\\"]); chdir('.\\Data\\')
import config


if __name__ == "__main__":
	config.win = config.Window.create_window()
	config.screen = config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)
	config.Advert_Cycle.advert_window(config.screen)

	config.Select_Card.cards_place()

config.win.mainloop()
