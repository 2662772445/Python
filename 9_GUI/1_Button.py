from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")

def hello():
    messagebox.showinfo("Hello Python", "Hello World")

B = Button(top, text = "Hello", bg = "grey", command = hello)
B.pack()

top.mainloop()
