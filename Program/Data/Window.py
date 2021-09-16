from tkinter import Tk, Frame, Button, Label, SOLID
import config


def create_window(DIMENSIONS = [900,600]):
    win = Tk()
    win.title("Welcome to 'Bank' ATM")
    win['bg'] = config.BLUE
    win.geometry(f"{DIMENSIONS[0]}x{DIMENSIONS[1]}+150+50")    
    win.minsize(DIMENSIONS[0], DIMENSIONS[1])
    win.maxsize(DIMENSIONS[0], DIMENSIONS[1])
    win.update()

    return win


def create_screen(win):
    ratio = win.winfo_height()/win.winfo_width()
    frm = Frame(win, bg='darkblue', highlightthickness=10, highlightbackground="#777777")
    frm.place(relx=ratio/2, rely=0.5, relwidth=ratio*0.95, relheight=0.95, anchor='center')
    
    return frm


def clear_screen(win):
    for child in win.winfo_children():
        child.destroy()


def control_press(action, screen=None):    
    if config.EN_NUMPAD:
        print(action)
        if action == "Accept":
            pass
        elif action == "Back":
            pass
        elif action == "Cancel":
            config.Message_Windows.transaction_ended_window(screen, 'CANCELLED')

    else: print("Numpad Disabled")


def num_press(n, entry=None):
    if config.EN_NUMPAD:
        print(type(n),n)
    
    else: print("Numpad Disabled")


def create_numpad(win, screen):
    ratio = win.winfo_height()/win.winfo_width()
    button_font = (None, 20)
    
    pad = Frame(win, bg='#777777')
    pad.place(relx=ratio+((1-ratio)/2), rely=0.45, relheight=0.45, relwidth=(1-ratio)*0.8, anchor='center')
    
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
    Button(control_keys, text="Back", font=(None, 10), bg="orange",
        command = lambda : control_press("Back")).grid(column=0, row=2, stick='nsew')
    Button(control_keys, text="Cancel", font=(None, 10), bg="red",
        command = lambda : control_press("Cancel",screen)).grid(column=0, row=3, stick='nsew')

    #Card Slot
    Frame(win, bg='#777777').place(relx=ratio+((1-ratio)/2), rely=0.825, relheight=0.1, relwidth=(1-ratio)*0.8, anchor='center')
    Frame(win, bg='#222222').place(relx=ratio+((1-ratio)/2), rely=0.825, relheight=0.015, relwidth=(1-ratio)*0.8*0.85, anchor='center')



if __name__ == "__main__":
    win = create_window()
    screen = create_screen(win)
    Button(win, text='Clear it', command= lambda: clear_screen(screen)).place(relx=0.8, rely=0.05, anchor='n', width=100)
    Button(win, text='Exit', command= exit).place(relx=0.8, rely=0.1, anchor='n', width=100)
    create_numpad(win, screen)
    Label(screen, text="Hello", font=(None,50)).place(relx=0.5, rely=0.5, anchor='center')
    win.mainloop()
