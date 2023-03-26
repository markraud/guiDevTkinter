import tkinter as tk
from tkinter import ttk 


def greet():
    print(f"Hello, {userName.get() or 'World'}!")

root = tk.Tk()

userName = tk.StringVar()

nameLabel = ttk.Label(root, text="Name: ")
nameLabel.pack(side="left", padx=(0, 10))
nameEntry = ttk.Entry(root, width=15, textvariable=userName)
nameEntry.pack(side="left")
nameEntry.focus()


greetButton = ttk.Button(root, text="Greet", command=greet)
# greetButton.pack(side="left", fill="x", expand=True)
greetButton.pack(side="left")


quitButton = ttk.Button(root, text="Quit", command=root.destroy)
# quitButton.pack(side="left", fill="x", expand=True)
quitButton.pack(side="right")

root.mainloop()