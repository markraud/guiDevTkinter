import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand="true")

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(side="top", ipadx=10, ipady=10, fill="both", expand="true")

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="black", fg="white")
rectangle_2.pack(side="left", ipadx=10, ipady=10, fill="both", expand="true")

root.mainloop()