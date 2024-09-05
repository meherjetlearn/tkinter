# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('200x200')
root.config(background="gray")

# Create a Button
btn = Button(root, text='Click me !', bd='5',background="cyan",command=root.destroy)

# Set the position of button on the top of window.
#try side = bottom, right, left

btn.pack(side='top')

root.mainloop()