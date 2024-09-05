from tkinter import *
#combobox is defined inside ttk
from tkinter.ttk import *
  
# Creating tkinter window 
window = Tk() 
window.title('Pizza App')

si=StringVar
# label text for title 
title=Label(window, text = "Welcome to Pizza Hut")
# label 
caption1=Label(window, text = "Select your fav pizza")
caption2=Label(window, text = "Enter Quantity")
caption3=Label(window, text = "")

#place labels
title.grid(row = 0, column = 0,columnspan = 3, pady=25)
caption1.grid(column = 0,row = 1,padx=40)
caption2.grid(column = 0,row = 2,padx=40)
caption3.grid(column = 0,row = 3,columnspan = 3,padx=40)
  
# Combobox creation 
pizzatype = StringVar()
pizzatypes=Combobox(window,textvariable = pizzatype,width=8)   
# Adding combobox drop down list 
pizzatypes['values'] = ["veg extravaganza", "Garden", "margarita"]

quantity = StringVar()
quantities=Combobox(window,textvariable = quantity,width=8)   
quantities['values'] = ["1", "2", "3"]





#radio buttons
size = StringVar()
r1=Radiobutton(window,text="S",variable=size,value="s",)
r2=Radiobutton(window,text="M",variable=size,value="m")
r3=Radiobutton(window,text="L",variable=size,value="l")
#set the default value
size.set("s")


#place radiobuttons and combobox
pizzatypes.grid(column = 1, row = 1, pady=10)
quantities.grid(column = 1, row = 2)
r1.grid(column = 2, row = 1)
r2.grid(column = 2, row = 2,padx=10)
r3.grid(column = 2, row = 3,padx=10)
caption3.grid(row=5,column=1)


def generatetext():
    if(size.get()=="s"):
        si="Small"
    
    if(size.get()=="m"):
        si="medium"
    
    
    if(size.get()=="l"):
        si="large"
    
    caption3.configure(text="You ordered " +quantity.get() +" "+  pizzatype.get() + " "+ si + " Pizza(s)")

#create button and result table
generateButton=Button(window,text="Generate",command=generatetext)
table=Label(window,anchor="center")

#place button and result table
generateButton.grid(row=4,column=1)
table.grid(row=5,column=0, pady = 25)


window.mainloop() 