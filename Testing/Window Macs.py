from tkinter import Tk, Frame, Button


BLUE = "#3380cc"

def create_window(DIMENSIONS = [400,600]):
    win = Tk()
    win.title("Welcome to 'Bank' ATM")
    win['bg'] = BLUE
    win.geometry(f"{DIMENSIONS[0]}x{DIMENSIONS[1]}+300+50")
    #win.minsize(DIMENSIONS[0], DIMENSIONS[1])
    #win.maxsize(DIMENSIONS[0], DIMENSIONS[1])

    return win


def clear_window(win):
    for child in win.winfo_children():
        child.destroy()


def screen(win):
    frm = Frame(win, bg='#888888')
    frm.place(relx=0.5, rely=0.025, relwidth=0.9, relheight=0.575, anchor='n')
    return frm


def create_numpad(win):
    button_font = (None, 20)
    
    pad = Frame(win, bg='#888888')
    pad.place(relx=0.5, rely=0.975, relheight=0.35, relwidth=0.9, anchor='s')
    
    num_keys = Frame(pad, bg='#aaaaaa')
    num_keys.place(relx=0.05, rely=0.5, relheight=0.9, relwidth=0.65, anchor='w')
    num_keys.columnconfigure([0,1,2], weight=1)
    num_keys.rowconfigure([0,1,2,3], weight=1)

    x = y = 0
    for key in range(1,10):
        Button(num_keys, text=f"{key}", font=button_font, border=0).grid(column=x, row=y, stick='nsew')
        x+=1
        if x%3==0:
            x=0; y+=1
    Button(num_keys, text="0", font=button_font, border=0).grid(column=x+1, row=y, stick='nsew')

    control_keys = Frame(pad, bg='#aaaaaa')
    control_keys.place(relx=0.95, rely=0.5, relheight=0.9, relwidth=0.2, anchor='e')
    control_keys.columnconfigure(0, weight=1)
    control_keys.rowconfigure([0,1,2], weight=1)

    Button(control_keys, text="Accept", font=(None, 10), border=0, bg="lightgreen").grid(column=0, row=0, stick='nsew')
    Button(control_keys, text="Back", font=(None, 10), border=0, bg="orange").grid(column=0, row=1, stick='nsew')
    Button(control_keys, text="Cancel", font=(None, 10), border=0, bg="red").grid(column=0, row=2, stick='nsew')


if __name__ == "__main__":
    from time import sleep
    win = create_window()
    screen(win)
    Button(win, text='Clear it', border=0, command= lambda: clear_window(win)).place(relx=0.5, rely=0.05, anchor='n', width=100)
    Button(win, text='Exit', border=0, command= exit).place(relx=0.5, rely=0.1, anchor='n', width=100)
    create_numpad(win)
    win.mainloop()
