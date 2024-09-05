from tkinter import *

# Create a GUI window
window = Tk()
window.title('Currency Converter')

# Function to convert weight
# given in kg to grams, pounds
# and ounces
def from_rupees():
    # convert kg to gram
    dollar = float(rupees_value.get())*83

    # convert kg to pound
    

    # Enters the converted weight to
    # the text widget
#delete('1.0', which represents line 1, character 0) to the end of the text widget (tk.END).
#t1.delete is to clear the previous content, 
    #target_value.delete("1.0", END)
    target_value.config(text=str(dollar))

  

title1 = Label(window, text="Rs->$ converter")
# Create the Label widgets
rupees_label = Label(window, text="Source Currency Amount Rs.")
rupees_value = Entry(window, width=26)

# Create the Text Widgets
targert_label = Label(window, text="Targeted Currency Amount $")
#target_value= Text(window, height=1, width=20)
target_value= Label(window, )

# Create the Button Widget
b1 = Button(window, text="Convert", command=from_rupees)

# grid method is used for placing
# the widgets at respective positions
# in table like structure
title1.grid(row=0,column=1)
rupees_label.grid(row=1, column=0)
rupees_value.grid(row=1, column=2)
targert_label.grid(row=2, column=0)
target_value.grid(row=2, column=2)
b1.grid(row=3,column=1)

# Start the GUI
window.mainloop()