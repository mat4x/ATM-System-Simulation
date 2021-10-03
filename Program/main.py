from os import chdir, getcwd
import sys
import platform

if platform.system() == "Windows":
	sys.path.extend([getcwd()+".\\Data\\", getcwd()+".\\Data\\images\\"]); chdir('.\\Data\\')	#Windows
else: sys.path.extend([getcwd()+"./Data/", getcwd()+"./Data/images/"]); chdir('./Data/')		#Mac OS
import config



def start():
	config.win = config.Window.create_window()
	config.screen = config.Window.create_screen(config.win)
	config.Window.create_numpad(config.win, config.screen)
	config.Advert_Cycle.advert_window(config.screen)
	config.Select_Card.cards_place()


if __name__ == "__main__":
	start()
	config.win.mainloop()
