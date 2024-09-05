from tkinter import*
import tkinter.font as font
import random

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("550x330")

playerscore = 0
computerscore = 0
rps = [("Rock",0),("Paper",1),("Scissors",2)]

"""print(rps[1])""" #how to acces tuples
def computer_win():
    global computerscore,playerscore
    computerscore = computerscore + 1
    winnerlabel.config(text = "Computer Won !!")
    player_score_label.config(text = "Player Score:" +str (playerscore))
    computer_score_label.config(text = "Computer Score:" +str(computerscore))

def player_win():
    global computerscore,playerscore
    playerscore = playerscore + 1
    winnerlabel.config(text = "Player Won!!")
    player_score_label.config(text = "Player Score:" +str (playerscore))
    computer_score_label.config(text = "Computer Score:" +str(computerscore))

def tie():
    global computerscore,playerscore
    winnerlabel.config(text = "Tie!!")
    print("tie")
    
def game(playerinput):
    print(playerinput)
    computerinput = (random.choice(rps))
    print(computerinput)
    if playerinput == computerinput:
        tie()
    


gametitle = Label(window,text = "Rock Paper Scissors",
                    font = font.Font(size = 25)).place(x = 135,y = 25)

winnerlabel = Label(window,text = "Lets Start!",
                    font = font.Font(size = 15), fg = "green")
winnerlabel.place(x = 200, y = 75)
#tell this to adam , .place should be given seperately  like line no 47
"""winnerlabel = Label(window,text = "Lets Start!",
                    font = font.Font(size = 15), fg = "green").place(x = 200, y = 75)"""


input_frame = Frame(window)
input_frame.place(x = 20, y = 110)

options = Label(input_frame,text = "Your options:",
                font = font.Font(size = 12),fg = "grey")
rock_btn = Button(input_frame,text = "Rock", width = 10,padx = 8, pady = 5,command = lambda:game(rps[0]))
                    #padding creates more space inside the button
paper_btn = Button(input_frame,text = "Paper", width = 10,padx = 8, pady = 5,command = lambda:game(rps[1]))
scissors_btn = Button(input_frame,text = "Scissors", width = 10,padx = 8, pady = 5,command = lambda:game(rps[2]))

score_frame = Frame(window)
score_frame.place(x = 20 , y = 220)
scorelabel = Label(score_frame,text = "Score:",
                   font = font.Font(size = 12),fg = "grey")

player_chose_label = Label(score_frame,text = "Your Selection: ",
                           font = font.Font(size = 12),padx = 55, pady = 5)
player_score_label = Label(score_frame,text = "Player Score: ",
                           font = font.Font(size = 12),padx = 35,pady = 5)
computer_chose_label = Label(score_frame,text = "Computer Selection: ",
                           font = font.Font(size = 12),padx = 55, pady = 5)
computer_score_label = Label(score_frame,text = "Computer Score: ",
                           font = font.Font(size = 12),padx = 35,pady = 5)

options.grid(row = 0, column = 0)
rock_btn.grid(row = 1, column = 1)
paper_btn.grid(row = 1, column = 2)
scissors_btn.grid(row = 1, column = 3)

scorelabel.grid(row = 0, column = 0)
player_score_label.grid(row = 1, column = 1)
player_chose_label.grid(row = 1,column = 2)

computer_chose_label.grid(row = 2, column = 1)
computer_score_label.grid(row = 2, column = 2)


window.mainloop()