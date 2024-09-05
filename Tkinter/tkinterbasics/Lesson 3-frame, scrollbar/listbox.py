from tkinter import *

# create a root window.
top = Tk()
top.title("My favorite Dishes")
# create listbox object
#activestyle option is used with the Button widget 
#to specify the appearance of the button when it is active or under focus.options are none,underline and dotbox 
listbox = Listbox(top, height=10,
                  width=15,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="yellow")

# Define the size of the window.
top.geometry("300x250")

# Define a label for the list.
label = Label(top, text=" FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

# pack the widgets
label.pack()
listbox.pack()

# Display untill User
# exits themselves.
top.mainloop()