# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('400x400')
root.config(background="gray")

# Create a Button
btn1 = Button(root, text='Click me !', bd='5',background="cyan",command=root.destroy)
btn2 = Button(root, text='Click me !', bd='5',background="cyan",command=root.destroy)
btn3 = Button(root, text='Click me !', bd='5',background="cyan",command=root.destroy)
btn4 = Button(root, text='Click me !', bd='5',background="cyan",command=root.destroy)
# Set the position of button on the top of window.
#try side = bottom, right, left

btn1.pack(side='top')
btn2.pack(side='bottom')
btn3.pack(side='left')
btn4.pack(side='right')

root.mainloop()