from tkinter import *


root = Tk()
root.geometry("300x400")

l0 = Label(root, text = "Create an account", font = "time 20")
l0.pack()

l1 = Label(root, text = "Email address", font = "time 10")
l1.place(x = 23, y = 70)
l2 = Label(root, text = "Phone(recommended)", font = "time 10")
l2.place(x = 23, y = 160)

root.mainloop()
