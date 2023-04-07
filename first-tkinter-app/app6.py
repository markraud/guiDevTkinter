import tkinter as tk
from tkinter import ttk 


def greet():
    print(f"Hello, {userName.get() or 'World'}!")

root = tk.Tk()

userName = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20,0))
input_frame.pack(fill="both")

nameLabel = ttk.Label(input_frame, text="Name: ")
nameLabel.pack(side="left", padx=(0, 10))
nameEntry = ttk.Entry(input_frame, width=15, textvariable=userName)
nameEntry.pack(side="left")
nameEntry.focus()

buttons = ttk.Frame(root, padding=(20,10))
buttons.pack(fill="both")

greetButton = ttk.Button(buttons, text="Greet", command=greet)
greetButton.pack(side="left", fill="x", expand=True)
quitButton = ttk.Button(buttons, text="Quit", command=root.destroy)
quitButton.pack(side="right", fill="x", expand=True)

root.mainloop()