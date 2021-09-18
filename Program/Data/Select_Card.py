from tkinter import Tk, Frame, Button, Entry, Label, Toplevel
from PIL import Image, ImageTk
import config


def remove_card(crd):
    if config.CARD_REMOVE:
        crd.destroy()
        config.CARD_REMOVE = False
        cards_place()
    else: print("Can't Remove Card")


def card_authenticate(card):
    from Classes import Account, Card

    accs = [Account(101010, "Personal", "Mayur Sharma", 50000, 202020, 1001),           ## Have to work here
            Account(102010, "Business", "Ajay Patil",  100000, 202021, 1110),
            Account(103010, "Personal", "Amar Patel",  200200, 203021, 2110),
            Account(104010, "Business", "Sahil Verma", 123000, 204021, 9810),
            Account(105010, "Personal", "Nikhil Rao",  100456, 205021, 9130),
            Account(106010, "Personal", "Sakaar Shah", 105010, 206021, 9220) ]
    
    for acc in accs:
        if card.card_no == acc.card_no:
            return acc
    return None


def card_select(win2,card):
    config.CURR_USER_ACC = card_authenticate(card)
    if not(config.CURR_USER_ACC):
        config.Message_Windows.transaction_ended_window("UNREADABLE")
        return

    #else
    win2.destroy()
    config.EN_NUMPAD = True
    
    ratio = config.win.winfo_height()/config.win.winfo_width()
    global CARD_INSERTED_IMG
    img = ".\\images\\Card_inserted.gif"
    size = [int(d/1.5) for d in Image.open(img).size]
    CARD_INSERTED_IMG = ImageTk.PhotoImage(Image.open(img).resize(size))

    card_btn = Button(config.win, image=CARD_INSERTED_IMG, activebackground= '#555555', bg='#777777', border=0, command=lambda: remove_card(card_btn))
    card_btn.place(relx=ratio+((1-ratio)/2), rely=0.825, anchor='n')

    print(config.CURR_USER_ACC.name, config.CURR_USER_ACC.card_PIN)
    config.CYCLE = False

    #call Enter PIN Screen window here / Card Authentication
    config.PIN_Screen.enter_pin_screen()


def cards_place(DIMENSIONS=[350,450]):

    #Creating card selecting window
    win = Toplevel()
    win.title("Select Card")
    win['bg'] = config.BLUE
    win.geometry(f"{DIMENSIONS[0]}x{DIMENSIONS[1]}+915+100")
    win.update()
    win.columnconfigure([0,1], weight=1)
    win.rowconfigure([0,1,2], weight=1)

    #get accounts from file
    accounts = get_cards()

    
    #import card image for button
    global CARD_IMG
    card_img = ".\\images\\Card_2.gif"
    CARD_IMG = ImageTk.PhotoImage(Image.open(card_img).resize((120,90), Image.ANTIALIAS))

    #place cards on screen
    r = c = 0
    for acc in accounts:
        '''Button(win, text=acc.name, image=CARD_IMG, bg=config.BLUE, border=0, activebackground=config.BLUE,
            command = lambda x=acc : card_select(win,x)).grid(row=r, column=c)'''
        
        frm = Frame(win, bg=config.BLUE);  frm.grid(row=r, column=c)

        Button(frm, text=acc.name, image=CARD_IMG, bg=config.BLUE, border=0, activebackground=config.BLUE,
            command = lambda x=acc : card_select(win,x)).pack()
        Label(frm, text=acc.name, bg=config.BLUE).pack()

        c+=1
        if c==2:
            r+=1; c=0
    return win


def get_cards(file=None):
    from Classes import Card

    cards =[Card("Mayur Sharma",202020, "Available", 0),
            Card("Ajay Patil",  202021, "Available", 0),
            Card("Amar Patel",  203021, "Blocked",   0),
            Card("Sahil Verma", 204021, "Available", 0),
            Card("Nikhil Rao",  205021, "Blocked",   0),
            Card("Invalid Card", 700021, "Available", 0) ]

    return cards

    
if __name__ == "__main__":

    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)

    win2 = cards_place()

    config.win.mainloop()
