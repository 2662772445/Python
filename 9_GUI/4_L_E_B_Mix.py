from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x500")

#label
l0 = Label(root, text = "Create an account", font = ('italic', 20, 'bold'))
l0.pack()

l1 = Label(root, text = "Email address", font = "time 10")
l1.place(x = 23, y = 70)
l2 = Label(root, text = "Phone(recommended)", font = "time 10")
l2.place(x = 23, y = 160)
l3 = Label(root, text = "Password", font = "time 10")
l3.place(x = 23, y = 250)

#Entry
E1 = Entry(root, width = "31", font = "time 15")
E1.place(x = 25, y = 90)
E2 = Entry(root, width = "31", font = "time 15")
E2.place(x = 25, y = 180)
E3 = Entry(root, width = "31", font = "time 15")
E3.place(x = 25, y = 270)

#Button
def hello():
   messagebox.showinfo( "Hello Python", "Hello World")
B = Button(root, text = "Create Account", bg = "blue", fg = "white", width = "37", font = "time 12", command = hello)
B.place(x = 25, y = 350)

root.mainloop()
