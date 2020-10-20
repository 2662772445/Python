from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x500")

#Entry
E1 = Entry(root, bd = 2, width = "31", font = "time 15")
E1.place(x = 25, y = 90)
E2 = Entry(root, bd = 3, width = "31", font = "time 15")
E2.place(x = 25, y = 180)
E3 = Entry(root, bd = 4, width = "31", font = "time 15")
E3.place(x = 25, y = 270)

root.mainloop()
