#!/usr/bin/python3
"""Simple Calculator App"""

# Imports
import tkinter as tk
from tkinter.constants import SUNKEN

# Create the calculator window
root = tk.Tk()
root.title("Simple Calculator")

# Create a frame for the calculator
frame = tk.Frame(master=root, bg="skyblue", padx=10, pady=10, cursor="hand2")
frame.grid(row=0, column=0, padx=10, pady=10)

# Create a display entry widget
display = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=40, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=4, ipady=10, pady=5)

# Button click functions
def button_click(val):
    cur_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, cur_text + str(val))

# Clear display
def clear_display():
    display.delete(0, tk.END)

# Calculate function
def calculate():
    """Calculate the expression"""
    expression = display.get().replace('x', '*').replace('^', '**')

    try:
        if '%' in expression:
            parts = expression.split('%')
            if len(parts) == 2 and parts[0].strip().isdigit() and parts[1].strip().isdigit():
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 * (num2 / 100)
            else:
                raise ValueError("Invalid percentage operation")
            
        else:
            without_zeros = ''
            temp = ''
            for char in expression:
                if char in '+-*/':
                    if temp:
                        without_zeros += temp.lstrip('0') or '0'
                    without_zeros += char
                    temp = ''
                else:
                    temp += char
            if temp:
                without_zeros += temp.lstrip('0') or '0'
            
            result = eval(without_zeros)
        display.delete(0, tk.END)
        display.insert(0, str(result))

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Can't divide by 0")

    # Create buttons and hover effects
def on_enter(e):
    e.widget['background'] = 'white'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'


# Calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("x", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("clear", 5, 0), ("%", 5, 1), ("^", 5, 2), ("", 5, 3)
]

# Create and place buttons on the grid
for (text, row, col) in buttons:
    btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 18), fg="darkred",
                    command=lambda value=text: button_click(value) if text not in ["=", "clear"] else None)
    
    if text == "=":
        btn.config(command=calculate)
        btn.grid(row=row, column=col, sticky="nsew")
    elif text == "clear":
        btn.config(command=clear_display)
        btn.grid(row=row, column=col, sticky="nsew")
    else:
        btn.grid(row=row, column=col, sticky="nsew")
    
    # Bind hover events
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Run the main event loop
root.mainloop()