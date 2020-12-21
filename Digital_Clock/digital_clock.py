from tkinter import *
from tkinter.ttk import *
from time import strftime

# clock user interface
UI = Tk()
UI.title("Digital Clock")


# defining the time format
def time():
    time_format = strftime("%H: %M: %S %p")
    label.config(text=time_format)
    label.after(1000, time)


# variable to contain the clock
label = Label(UI, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()