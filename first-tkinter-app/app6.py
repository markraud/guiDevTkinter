import tkinter as tk
from tkinter import ttk 


def greet():
    print(f"Hello, {userName.get() or 'World'}!")

root = tk.Tk()
root.title("Greeter")

root.columnconfigure(0, weight=1)

userName = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20,0))
input_frame.grid(row=0, column=0,sticky="EW")

nameLabel = ttk.Label(input_frame, text="Name: ")
nameLabel.grid(row=0, column=0, padx=(0, 10))
nameEntry = ttk.Entry(input_frame, width=15, textvariable=userName)
nameEntry.grid(row=0, column=1,)
nameEntry.focus()

buttons = ttk.Frame(root, padding=(20,10))
buttons.grid(row=1, column=0, sticky="EW")
buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

greetButton = ttk.Button(buttons, text="Greet", command=greet)
greetButton.grid(row=0, column=0,sticky="EW")
quitButton = ttk.Button(buttons, text="Quit", command=root.destroy)
quitButton.grid(row=0, column=1,sticky="EW")

root.mainloop()