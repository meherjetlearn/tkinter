from tkinter import *

screen = Tk()
screen.title("Replit")
screen.geometry("450x300")
screen.config(background="black")

# the label for user_name
template = Label(screen,text="Pick a template").place(x=40,y=60)

# the label for user_password
entry = Label(screen,text="enter the template name").place(x=40,y=100)

createrepl = Button(screen,text="create a repl",bd="10", background="yellow").place(x=40,y=130)

user_name_input_area = Entry(screen,width=30).place(x=150,y=60)

user_password_entry_area = Entry(screen,show='*',width=30).place(x=150,y=100)

screen.mainloop()