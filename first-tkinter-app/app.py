import tkinter as tk
from tkinter import ttk         #allows our app to look native in either windows or mac


root = tk.Tk()
ttk.Label(root, text="Hello, World!", padding=(30,10)).pack()

root.mainloop()