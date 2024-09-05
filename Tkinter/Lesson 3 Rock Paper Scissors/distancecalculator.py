from tkinter import *
import tkinter.font as font

#Function to Convert Celsius to Fahrenheit
def calculate():
    distance = float(time_value.get()) * float(speed_val.get())

    output_msg.config(text = 'Distance : ' + str(distance) + " KM")
    

my_window = Tk()
my_window.title("Distance Calculator")

#Displaying heading inside window
description = Label(text = 'Distance Calculator', font = font.Font(size = 20), fg = "grey")
description.pack()

frame = Frame(my_window)
frame.pack(pady = 20)

#entry box to enter temperature in celsius
message_one = Label(frame, text = 'Enter time in hr : ', font = font.Font(size = 10))
message_one.grid(row = 0, column = 0)

time_value = Entry(frame)
time_value.grid(row = 0, column = 1)

message_two = Label(frame, text = 'Enter speed in km : ', font = font.Font(size = 10))
message_two.grid(row = 1, column = 0)

speed_val = Entry(frame)
speed_val.grid(row = 1, column = 1)

#To Display Error Message

#To Display the Output
output_msg = Label(frame, font = font.Font(size = 12))
output_msg.grid(row = 2, column = 0, columnspan = 2, pady = 10)

#Submit Button
submit_btn = Button(frame, text = 'Calculate', width = 30, fg = "black", bg = "light green", bd = 0, padx = 20, pady = 10, command = calculate)
submit_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10)

my_window.geometry('500x250')
my_window.mainloop()