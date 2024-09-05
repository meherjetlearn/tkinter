from tkinter import *

root = Tk()
root.geometry("150x200")

w = Label(root, text='HelloHello',
          font="50")

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack(side=RIGHT,
                fill=Y)
#yscrollcommand - This option is crucial for connecting the Listbox to the Scrollbar, enabling scrolling functionality.
mylist = Listbox(root,
                 yscrollcommand=scroll_bar.set)

for i in range(1, 26):
    mylist.insert(END, "Hi " + str(i))
#ill=BOTH option specifies that the Listbox should expand both horizontally and vertically 
#to fill any available space within its container
mylist.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=mylist.yview)

root.mainloop()