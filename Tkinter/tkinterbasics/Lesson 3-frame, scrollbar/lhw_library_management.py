import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar

def add_book():
    book_title = title_entry.get()
    book_author = author_entry.get()
    book_genre = genre_spinbox.get()
    book_status = status_spinbox.get()
    
    if book_title and book_author and book_genre and book_status:
        book_info = f"{book_title} by {book_author} - Genre: {book_genre}, Status: {book_status}"
        book_listbox.insert(tk.END, book_info)
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Book added successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def remove_book():
    selected_index = book_listbox.curselection()
    if selected_index:
        book_listbox.delete(selected_index)
        messagebox.showinfo("Success", "Book removed successfully!")
    else:
        messagebox.showerror("Error", "Please select a book to remove.")

# Create main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x300")

# Labels
tk.Label(root, text="Title:").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Author:").pack()
author_entry = tk.Entry(root)
author_entry.pack()

tk.Label(root, text="Genre:").pack()
genre_spinbox = tk.Spinbox(root, values=("Fiction", "Non-fiction", "Fantasy", "Science Fiction"))
genre_spinbox.pack()

tk.Label(root, text="Status:").pack()
status_spinbox = tk.Spinbox(root, values=("Available", "Checked Out", "Reserved"))
status_spinbox.pack()

# Buttons
add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.pack()

remove_button = tk.Button(root, text="Remove Book", command=remove_book)
remove_button.pack()

# Book Listbox with Scrollbar
book_frame = tk.Frame(root)
book_frame.pack(fill=tk.BOTH, expand=True)

book_listbox = tk.Listbox(book_frame)
book_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

book_scrollbar = tk.Scrollbar(book_frame, orient=tk.VERTICAL, command=book_listbox.yview)
book_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

book_listbox.config(yscrollcommand=book_scrollbar.set)

# Progress Bar
progress = Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='indeterminate')
progress.pack(pady=10)
progress.start(10)

root.mainloop()
