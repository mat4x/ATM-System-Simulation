from tkinter import Tk,Button, Entry, Label, Toplevel
from PIL import Image, ImageTk
import config


def remove_card(crd):
    if config.CARD_REMOVE:
        crd.destroy()
        config.CARD_REMOVE = False
        cards_place()

    else: print("Can't Remove Card")



def card_select(win2,acc):
    win2.destroy()

    config.EN_NUMPAD = True
    
    ratio = config.win.winfo_height()/config.win.winfo_width()
    global CARD_INSERTED_IMG
    img = ".\\images\\Card_inserted.gif"
    size = [int(d/1.5) for d in Image.open(img).size]
    CARD_INSERTED_IMG = ImageTk.PhotoImage(Image.open(img).resize(size))

    card_btn = Button(config.win, image=CARD_INSERTED_IMG, bg='#777777', border=0, command=lambda: remove_card(card_btn))
    card_btn.place(relx=ratio+((1-ratio)/2), rely=0.825, anchor='n')

    config.USER_ACC = acc
    print(acc.name)

    #call Enter PIN Screen window here / Card Authentication
    config.PIN_Screen.enter_pin_screen()


def cards_place(DIMENSIONS=[350,450]):

    #Creating card selecting window
    win = Toplevel()
    win.title("Select Card")
    win['bg'] = config.BLUE
    win.geometry(f"{DIMENSIONS[0]}x{DIMENSIONS[1]}+900+100")
    win.update()
    win.columnconfigure([0,1], weight=1)
    win.rowconfigure([0,1,2], weight=1)

    #get accounts from file
    accounts = read_accounts()
    
    #import card image for button
    global CARD_IMG
    card_img = ".\\images\\Card_2.gif"
    CARD_IMG = ImageTk.PhotoImage(Image.open(card_img).resize((120,90), Image.ANTIALIAS))

    #place cards on screen
    r = c = 0
    for acc in accounts:
        Button(win, text=acc.name, image=CARD_IMG, bg=config.BLUE, border=0, activebackground=config.BLUE,
            command = lambda x=acc : card_select(win,x)).grid(row=r, column=c)
        c+=1
        if c==2:
            r+=1; c=0
    return win


def read_accounts(file=None):
    from Classes import Account
    accs = [Account(101010, "Personal", "Mayur Sharma", 50000, 202020, 1001),
            Account(102010, "Business", "Ajay Patil",  100000, 202021, 1110),
            Account(103010, "Personal", "Amar Patel",  200200, 203021, 2110),
            Account(104010, "Business", "Sahil Verma", 123000, 204021, 9810),
            Account(105010, "Personal", "Nikhil Rao",  100456, 205021, 9130),
            Account(106010, "Personal", "Sakaar Shah", 105010, 206021, 9220) ]

    return accs

    
if __name__ == "__main__":


    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)

    win2 = cards_place()
    win2.mainloop()
