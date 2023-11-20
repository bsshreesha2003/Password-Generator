import tkinter as tk
from tkinter import StringVar
import random
import string

def generate_password():
    password_length = int(length_var.get())

    if difficulty_var.get() == "Easy":
        characters = string.ascii_letters
    elif difficulty_var.get() == "Medium":
        characters = string.ascii_letters + string.digits
    elif difficulty_var.get() == "Strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(password_length))
    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")

difficulty_var = StringVar()
length_var = StringVar()
password_var = StringVar()

difficulty_var.set("Easy")
length_var.set("8")

difficulty_label = tk.Label(root, text="Select Difficulty:")
difficulty_menu = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Strong","Very Strong")
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root, textvariable=length_var)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
password_label = tk.Label(root, text="Generated Password:")
password_display = tk.Entry(root, textvariable=password_var, state='readonly')

difficulty_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
difficulty_menu.grid(row=0, column=1, padx=10, pady=10, sticky='w')
length_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
length_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
generate_button.grid(row=2, column=0, columnspan=2, pady=10)
password_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
password_display.grid(row=3, column=1, padx=10, pady=10, sticky='w')

root.mainloop()
