from tkinter import Tk, Entry, Button, Label

def reset():
    file = open("Machine_info.txt", 'w')
    file.write("online\nKharghar\n200000")
    file.close()

def write_data():
    print(info)
    file = open("Machine_info.txt", 'w')
    file.write('\n'.join(info))
    file.close()

def set_status(status):
    info[0] = status

def add_cash():
    info[2] = str(min(500000, float(info[2])+float(e.get())))

if __name__ == "__main__":
    win = Tk()
    win.title("ATM controller")
    info = open("Machine_info.txt").read().split('\n')

    win.columnconfigure([0,1,2], weight=1)
    win.rowconfigure([0,1,2,3,4], weight=1)

    Label(win, text="ATM Machine Control",font=(None,20)).grid(row=0, column=0, columnspan=3, sticky='nsew')
    Label(win, text="Status",font=(None,12)).grid(row=1, column=0, sticky='w')
    Button(win, text="Online", fg="darkgreen", command=lambda: set_status("online")).grid(row=1, column=1, sticky='nsew')
    Button(win, text="Offline", fg="darkred", command=lambda: set_status("offline")).grid(row=1, column=2, sticky='nsew')
    
    Label(win, text="Add Cash",font=(None,12)).grid(row=2, column=0, sticky='w')
    e = Entry(win)
    e.grid(row=2, column=1, sticky='nsew')
    Button(win, text="Confirm", command=add_cash).grid(row=2, column=2, sticky='nsew')

    Button(win, text="Update Information",font=(None,12), bg='lightgrey', command=write_data).grid(row=3, column=0, columnspan=3, sticky='nsew')
    Button(win, text="Reset",font=(None,12), command=reset).grid(row=4, column=0, columnspan=3, sticky='nsew')

    win.mainloop()
    
