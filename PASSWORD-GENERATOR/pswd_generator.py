#!/usr/bin/python3
"""Password Generator using tkinter"""

# Imports
import tkinter as tk
import pyperclip
import string
import random


# Create the instance of the tkinter
root = tk.Tk()
root.title("Password Generator")

# Create the frame
frame = tk.Frame(master=root, bg="skyblue", padx=70, pady=100, cursor="hand2", width=300, height=300)
frame.grid(row=0, column=0, padx=10, pady=10)

# Create the title of the generator
title_label = tk.Label(frame, text="Paswword Generator", fg='white', bg='black', font=('Arial', 12, 'bold'))
title_label.grid(row=0, column=1)

# Create password label and entry
pswd_label = tk.Label(frame, text="Password")
pswd_label.grid(row=1, padx=10, pady=2, sticky='w')
pswd_entry = tk.Entry(frame, width=30)
pswd_entry.grid(row=1, column=1)

# Create length label and entry
len_label = tk.Label(frame, text="Length")
len_label.grid(row=2, padx=10, pady=2, sticky='w')
len_entry = tk.Entry(frame, width=30)
len_entry.grid(row=2, column=1)

# Functions
def pswd_generator(pswd_len):
    """Function to generate pswd"""
    try:
        pswd_len = int(pswd_len)
        if pswd_len <= 0:
            raise ValueError
        password = ''
        selection_list = string.ascii_letters + string.digits + string.punctuation

        for _ in range(pswd_len):
            password += '' .join(random.choices(selection_list))

        pswd_entry.delete(0, tk.END)
        pswd_entry.insert(0, password)
    except Exception:
        pswd_entry.delete(0, tk.END)
        pswd_entry.insert(0, "Invalid number")

def copy_pswd():
    """Copy password"""
    copied_pswd = pswd_entry.get()
    pyperclip.copy(copied_pswd)

# Create buttons and hover effects
def on_enter(e):
    e.widget['background'] = 'white'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'

# Buttons
copy_button = tk.Button(frame, text="Copy", command=copy_pswd)
copy_button.grid(row=1, column=2, padx=10, pady=2, sticky='e')
generate_button = tk.Button(frame, text="Generate", command=lambda: pswd_generator(len_entry.get()))
generate_button.grid(row=2, column=2, padx=10, pady=2, sticky='e')

# Bind hover events
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

# Run the main event loop
root.mainloop()