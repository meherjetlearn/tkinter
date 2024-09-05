
# importing only  those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()
root.title('Menu Demonstration')

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
#tearoff is to remove dashed lines when menu is getting created
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding format Menu
format_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Format', menu=format_)
format_.add_command(label='Word Wrap', command=None)
format_.add_command(label='Font', command=None)


#adding submenu for font
fontsub = Menu(format_, tearoff=0)
fontsub.add_command(label='text size', command=None)
fontsub.add_command(label='color', command=None)

format_.add_cascade(label="font preferences",menu=fontsub)



# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

# display Menu
root.config(menu=menubar)
mainloop()

