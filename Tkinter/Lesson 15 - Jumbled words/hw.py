import tkinter
from tkinter import *
import random
from tkinter import messagebox

root = tkinter.Tk()

answers=["apple","mango","banana",'achieve','kolkata','evening','servant','receiver','london','ferrari','hollow','horror','master','morning','bottle','pen','router','copy','narrow','wide','dive','love','block','right','simple','deaf','single','knight','hope']

questions ={
"'What is middle of Paris ? '":     'R',

'Which word is spelt wrong in every dictionary?' : 'Wrong',

'What can you catch but not throw?' : 'Cold',

'What animal can run the fastest- an elephant, squirrel or a mouse?' : 'Elephant',

'I am an odd number, but if you take away just a single letter I become even. Can you guess my number?' : 'Seven',

'I am tall when I am young, and I am short when I am old, what am I?' : 'Candle',

'What is so fragile that saying its name breaks it?' :'Silence',

'What has four eyes but cant see? ': 'Mississippi',
}

words =list(questions.keys())

c=0
d=0
s = ""
l = Label(root)

def reset():
    global words, answers, num
    num=random.randrange(0,len(words),1)
    label.config(text = words[num])
    e1.delete(0, END)

def default():
    global words,answers,num
    label.config(text = words[num])
    

def checkans():
    global words, answers, num, c, d, s, l
    d=int(d)+1
    
    key = words[num]
    print(questions[key])
    var = e1.get() #getting the answer
    if var == questions[key]: #checking if the answer is right or not
        messagebox.showinfo("Congratulations", "It's the correct answer!!")
        c = int(c)+1
    else:
        messagebox.showerror("Sorry", "It's not the correct answer.")
    s = 'Score :' + str(c) + '/' + str(d)
    l.forget()
    l = Label(root, font=("Verdana", 20), text=s, bg="#000000", fg="#fff", )
    l.pack(side=LEFT)
    reset()


root.geometry("500x500+500+150")
root.title("Jumbled word game")
root.configure(background="#000000")

Label(root,text="JUMBLED WORD GAME",font = ("Verdana",28),bg = "#000000", fg = "#fff").pack(pady = 5)
label = Label(root,font = ("Verdana",22),bg = "#000000", fg = "#fff")
label.pack(pady = 30,ipady=10,ipadx=10) # created a label that will be shown on the box and the pack() helps in executing what i wrote in Label

ans = StringVar() #defining that this is a string variable
e1 = Entry(root,font = ("Verdana",20),textvariable = ans,)
e1.pack(ipady=5,ipadx=5) #created an input box
#ipad=internal padding in x is called ipadx and y is called ipady
Button(root,text = "Check",font = ("Comic sans ms",20),width = 10,bg="#333945",fg="#45CE30",relief = GROOVE,command = checkans,).pack(pady = 40) #created a submit button
Button(root,text = "Reset",font = ("Comic sans ms",20),width = 10,bg="#777E8B",fg="#E1DA00",relief = GROOVE,command = reset).pack() #created a reset button

default()

root.mainloop() #its like the main function