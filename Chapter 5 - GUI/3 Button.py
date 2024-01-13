import tkinter as tk
from tkinter import messagebox

box = tk.Tk()
box.geometry("400x400")
def click():
    messagebox.showinfo("hello", "Green Button Clicked")
a = tk.Button(box, text="yellow", activeforeground="yellow", activebackground="orange", pady=10)
b = tk.Button(box, text="Blue", activeforeground="blue", activebackground="orange", pady=10)
c = tk.Button(box, text="Green", activeforeground="Green", activebackground="orange", pady=10)
d = tk.Button(box, text="Red", activeforeground="Red", activebackground="orange", pady=10)
e = tk.Button(box, text="Exit", background="green",fg="red", pady=10, command=box.destroy).pack()

a.pack(side="top")
b.pack(side="left")
c.pack(side="right")
d.pack(side="bottom")

box.mainloop()