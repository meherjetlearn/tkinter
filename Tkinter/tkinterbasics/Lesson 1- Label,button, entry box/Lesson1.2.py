from tkinter import *

screen = Tk()
screen.title("Login Me")
screen.geometry("450x300")
screen.config(background="pink")

# the label for user_name
user_name = Label(screen,text="Username").place(x=40,y=60)

# the label for user_password
user_password = Label(screen,text="Password").place(x=40,y=100)

submit_button = Button(screen,text="Submit",bd="10", background="yellow").place(x=40,y=130)

user_name_input_area = Entry(screen,width=30).place(x=110,y=60)

user_password_entry_area = Entry(screen,show='*',width=30).place(x=110,y=100)

screen.mainloop()