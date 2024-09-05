from tkinter import messagebox

# Display an informational message box
messagebox.showinfo("Information", "This is an informational message.")

# Display a warning message box
messagebox.showwarning("Warning", "This is a warning message.")

# Display an error message box
messagebox.showerror("Error", "This is an error message.")

# Display a yes/no question dialog
result = messagebox.askquestion("Question", "Do you want to continue?")
if result == "yes":
    print("User clicked Yes")
else:
    print("User clicked No")