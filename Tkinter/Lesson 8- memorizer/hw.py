from tkinter import *
from tkinter.filedialog import *


#create the window
master = Tk()
#title of window
master.title("Memorizer")
master.geometry("550x600")






#Function to delete item from listbox
def changebg():
    # get selected line index
    index = listbox.curselection()
    print(listbox.get(index))
    master.configure(bg=listbox.get(index))
   
        





#create listbox and place on screen

frame = Frame(master)
scrollbar = Scrollbar(frame, orient = "vertical")
scrollbar.pack(side = RIGHT, fill = Y)

listbox = Listbox(frame,width=20, yscrollcommand=scrollbar.set, bg = 'red')
listbox.insert(0,"red")
listbox.insert(1,"green")
listbox.insert(2,"blue")


listbox.pack(side = LEFT, padx = 5)    
scrollbar.config(command=listbox.yview)
lDelete=Button(master,text="DELETE",command=changebg,width=15)
lDelete.pack(side = RIGHT , padx=5,pady=5)


frame.pack(side = LEFT)
#listbox.grid(row=2,column=0,columnspan=3,pady=20,padx=5)
#scrollbar.grid(row=2,column=2,columnspan=3, sticky='NS')


mainloop()