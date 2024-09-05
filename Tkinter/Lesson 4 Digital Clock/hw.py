# importing whole module
from tkinter import *
from tkinter.ttk import *
import random

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')


# This function is used to
# display time on the label
def time():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string,background=f'#{red:02x}{green:02x}{blue:02x}',
            foreground='white')
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='red',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()