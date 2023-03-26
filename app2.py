import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello World!")


root = tk.Tk()

greetButton = ttk.Button(root, text="Greet", command=greet)
greetButton.pack(side="left", fill="x", expand=True)

quitButton = ttk.Button(root, text="Quit", command=root.destroy)
quitButton.pack(side="left")

root.mainloop()
