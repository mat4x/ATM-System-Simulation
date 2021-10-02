from tkinter import Tk, Frame, Button, Label, SOLID
from PIL import Image, ImageTk
import config


def create_window(DIMENSIONS = [900,600]):
    win = Tk()
    win.title("Welcome to 'Bank' ATM")
    win['bg'] = config.BLUE
    win.geometry(f"{DIMENSIONS[0]}x{DIMENSIONS[1]}+10+50")
    win.minsize(DIMENSIONS[0], DIMENSIONS[1])
    win.maxsize(DIMENSIONS[0], DIMENSIONS[1])
    win.update()

    return win


def create_screen(win):
    ratio = win.winfo_height()/win.winfo_width()
    frm = Frame(win, bg=config.DARK_BLUE, highlightthickness=10, highlightbackground="#777777")
    frm.place(relx=ratio/2, rely=0.5, relwidth=ratio*0.95, relheight=0.95, anchor='center')
    
    return frm


def clear_screen(win):
    for child in win.winfo_children():
        child.destroy()


def control_press(action, screen=None):    
    if action == "Cancel" and config.CAN_TERMINATE:
        config.Message_Windows.transaction_ended_window('CANCELLED')

    elif config.EN_NUMPAD:
        if action == "Accept":
            if config.ENTRY_BOX.get() == '':print("Empty")###
            config.NEXT_WINDOW()
        elif action == "Back":
            config.ENTRY_BOX.delete(config.ENTRY_BOX.index("end") - 1)

    else: print("Actions Disabled")  ####


def num_press(n, entry=None):
    if config.EN_NUMPAD:
        try:
            if len( config.ENTRY_BOX.get() ) != config.TEXT_LIMIT:
                config.ENTRY_BOX.insert("end",  str(n))
            else:
                print("limit exceeded")
        except:
            print("No input value")
    
    else: print("Numpad Disabled")  ####


def create_numpad(win, screen):
    ratio = win.winfo_height()/win.winfo_width()
    button_font = (None, 20)
    
    pad = Frame(win, bg='#777777')
    pad.place(relx=ratio+((1-ratio)/2), rely=0.025, relheight=0.45, relwidth=(1-ratio)*0.8, anchor='n')
    
    num_keys = Frame(pad, bg='#aaaaaa')
    num_keys.place(relx=0.05, rely=0.5, relheight=0.9, relwidth=0.65, anchor='w')
    num_keys.columnconfigure([0,1,2], weight=1)
    num_keys.rowconfigure([0,1,2,3], weight=1)

    #Setting up numpad number buttons
    x = y = 0
    for key in range(1,10):
        Button(num_keys, text=f"{key}", font=button_font,
            command=lambda n=key: num_press(n)).grid(column=x, row=y, stick='nsew')
        x+=1
        if x%3==0:
            x=0; y+=1
    Button(num_keys, text="0", font=button_font,
        command=lambda n=key: num_press(0)).grid(column=x+1, row=y, stick='nsew')

    #Setting up numpad control buttons
    control_keys = Frame(pad, bg='#aaaaaa')
    control_keys.place(relx=0.95, rely=0.5, relheight=0.9, relwidth=0.2, anchor='e')
    control_keys.columnconfigure(0, weight=1)
    control_keys.rowconfigure([0,1,2,3,4], weight=1)

    Button(control_keys, text="Accept", font=(None, 10), bg="lightgreen",
        command = lambda : control_press("Accept")).grid(column=0, row=1, stick='nsew')
    Button(control_keys, text="Clear", font=(None, 10), bg="orange",
        command = lambda : control_press("Back")).grid(column=0, row=2, stick='nsew')
    Button(control_keys, text="Cancel", font=(None, 10), bg="red",
        command = lambda : control_press("Cancel",screen)).grid(column=0, row=3, stick='nsew')

    #Card Slot
    Frame(win, bg='#777777').place(relx=ratio+((1-ratio)/2)-0.04, rely=0.56, relheight=0.055, relwidth=(1-ratio)*0.7, anchor='center')
    Frame(win, bg='#222222').place(relx=ratio+((1-ratio)/2)-0.04, rely=0.56, relheight=0.015, relwidth=(1-ratio)*0.7*0.85, anchor='center')

    global card_ico
    card_ico = Image.open(".\\images\\Insert_card_ico.gif")
    card_ico = ImageTk.PhotoImage(card_ico.resize((40,40), Image.ANTIALIAS))
    Label(win, bg=config.BLUE, image=card_ico).place(relx=ratio+((1-ratio)/2)+0.125, rely=0.56, anchor='center')

    #Cash Dispenser
    Frame(win, bg='#777777').place(relx=ratio+((1-ratio)/2), rely=0.7, relheight=0.07, relwidth=(1-ratio)*0.95, anchor='center')
    Frame(win, bg='#222222').place(relx=ratio+((1-ratio)/2), rely=0.7, relheight=0.015, relwidth=(1-ratio)*0.9, anchor='center')

    #Receipt Printer
    Frame(win, bg='#777777').place(relx=ratio+((1-ratio)/2)-0.04, rely=0.85, relheight=0.055, relwidth=(1-ratio)*0.7, anchor='center')
    Frame(win, bg='#222222').place(relx=ratio+((1-ratio)/2)-0.04, rely=0.85, relheight=0.015, relwidth=(1-ratio)*0.7*0.85, anchor='center')



if __name__ == "__main__":
    win = create_window()
    screen = create_screen(win)
    Button(win, text='Clear it', command= lambda: clear_screen(screen)).place(relx=0.8, rely=0.05, anchor='n', width=100)
    Button(win, text='Exit', command= exit).place(relx=0.8, rely=0.1, anchor='n', width=100)
    create_numpad(win, screen)
    Label(screen, text="Hello", font=(None,50)).place(relx=0.5, rely=0.5, anchor='center')
    win.mainloop()
