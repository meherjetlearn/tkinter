from tkinter import *

screen = Tk()
screen.title(" Food delivery")
screen.geometry("450x500")
screen.config(background="red")

# the label for email
email = Label(screen,text="Username").place(x=40,y=60)
email_inp_area = Entry(screen,width=30).place(x=110,y=60)

# the label for user_password
user_password = Label(screen,text="Password").place(x=40,y=100)
user_password_entry_area = Entry(screen,show='*',width=30).place(x=110,y=100)


#

#q1
question1 = Label(screen,text="What food would you like: Pizza,Burger, Sandwich etc..",font=("Time",10))\
                .place(x=20,y=150)
question1_entry = Entry(screen,width=20).place(x=10,y=180)
question1_entry_quantity = Spinbox(screen, from_=0, to=10).place(x=200,y=180)

submit_button = Button(screen,text="Submit Order", background="yellow").place(x=80,y=220)

screen.mainloop()