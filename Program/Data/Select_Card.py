from tkinter import Tk, Frame, Button, Entry, Label, Toplevel, SOLID
from PIL import Image, ImageTk
import config


def remove_card(crd):
    if config.CARD_REMOVE:
        crd.destroy()
        config.CARD_REMOVE = False
        cards_place()
    else: print("Can't Remove Card")


def card_select(win2,card):
    if not(config.CYCLE): return

    win2.destroy()
    config.EN_NUMPAD = True
    config.CYCLE = False
    
    #place card
    config.win.geometry("+200+50")
    ratio = config.win.winfo_height()/config.win.winfo_width()
    
    global CARD_INSERTED_IMG
    img = ".\\images\\Card_inserted.gif"
    size = [int(d/1.8) for d in Image.open(img).size]
    CARD_INSERTED_IMG = ImageTk.PhotoImage(Image.open(img).resize(size))

    card_btn = Button(config.win, image=CARD_INSERTED_IMG, activebackground= '#555555', bg='#777777', border=0, command=lambda: remove_card(card_btn))
    card_btn.place(relx=ratio+((1-ratio)/2)-0.04, rely=0.5575, anchor='n')

    if card.card_status != "Available":
        print("Card is blocked")
        config.Message_Windows.transaction_ended_window("BLOCKED")
        return

    config.CURR_CARD = card
    config.CURR_USER_ACC = config.Data_Access.get_acc(str(card.card_no))            #Card Authentication Here
    
    if not(config.CURR_USER_ACC):
        config.Message_Windows.transaction_ended_window("UNREADABLE")
    
    #call Enter PIN Screen window here / Card Authentication
    else:
        print(config.CURR_USER_ACC.name, config.CURR_USER_ACC.card_PIN)
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

    #get cards from file
    cards = config.Data_Access.get_cards()

    
    #import card image for button
    global CARD_IMG
    '''card_img = ".\\images\\Card.gif"
    CARD_IMG = ImageTk.PhotoImage(Image.open(card_img).resize((120,90), Image.ANTIALIAS))'''

    card_img = Image.open(".\\images\\Card_sides.gif")
    w,h = card_img.size
    card_img = card_img.crop((0,0,w,340))
    CARD_IMG = ImageTk.PhotoImage(card_img.resize((135,90), Image.ANTIALIAS))

    #place cards on screen
    r = c = 0
    for card in cards:        
        frm = Frame(win, bg=config.BLUE);  frm.grid(row=r, column=c)

        Button(frm, text=card.name, image=CARD_IMG, bg=config.BLUE, border=1, activebackground=config.BLUE,
            command = lambda x=card : card_select(win,x)).pack()
        Label(frm, text=card.name, bg=config.BLUE).pack()

        c+=1
        if c==2:
            r+=1; c=0
    return win

    
if __name__ == "__main__":

    config.win = config.Window.create_window()
    config.screen = config.Window.create_screen(config.win)
    config.Window.create_numpad(config.win, config.screen)

    win2 = cards_place()

    config.win.mainloop()
