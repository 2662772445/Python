from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("250x400+700+100")
root.title("Hlw")
root.iconbitmap("E:\College\internet.png")


img = ImageTk.PhotoImage(Image.open("E:\College\img.jpg"))
lbl = Label(image=img)
lbl.pack()



btn = Button(root, text="Exit", command=root.quit)
btn.pack()

root.mainloop()
