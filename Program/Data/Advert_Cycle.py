from tkinter import Tk, Label, Button, BOTH, X, Y, PhotoImage
from PIL import Image, ImageTk
import config


def cycle_advert(screen, i=0):
    TIME = 4500
    #print("Cycling")
    screen['image'] = IMAGES[i]
    if i==len(IMAGES)-1: i=-1
    if config.CYCLE:
        screen.after(TIME, lambda x=i: cycle_advert(screen, i+1))


def advert_window(screen):
    config.Window.clear_screen(screen)
    config.win.geometry("+10+50")
    screen.update()
    config.CYCLE = True

    DIM = [int(i*1.0) for i in (screen.winfo_height(), screen.winfo_width())]
    adverts_label = Label(screen, bg='black')
    adverts_label.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor = 'center')
 
    global IMAGES
    folder = ".\\images\\" if config.PLATFORM == "Windows" else './images/'
    #files = ['Brawlhalla.gif', 'Hitman.gif', 'Raid.gif', 'Tomb-Raider.gif']
    files = ['Ad'+str(i)+'.jpg' for i in range(1,6)]
    IMAGES = [ImageTk.PhotoImage(i) for i in [Image.open(folder+img).resize((DIM[0],DIM[1]), Image.ANTIALIAS) for img in files]]

    screen.after(0, lambda : cycle_advert(adverts_label))


if __name__ == "__main__":

    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)
    advert_window(config.screen)
    config.win.mainloop()
