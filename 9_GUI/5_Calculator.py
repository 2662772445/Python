from tkinter import *


#==================================================================
opr = ""

def Clk(no):
    global opr
    opr = opr + str(no)
    txtinput.set(opr)

def Clr():
    global opr
    opr = ""
    txtinput.set(opr)   

def Eql():
    global opr
    ans = str(eval(opr))
    txtinput.set(ans)   
    opr = ""

#==================================================================


root = Tk()
root.geometry("250x400+600+100")
root.resizable(0, 0)
root.title("Calculator")


txtinput = StringVar()

#LABEL

lb1 = Label(
    root, 
    text = "Label", 
    anchor = SE,  
    font = ("verdana", 20), 
    bg = "grey", 
    fg = "#ffffff",
    textvariable = txtinput,
)
lb1.pack(expand=True, fill="both", )

"""
txt = Entry(
    root, 
    font=('arial', 20, "bold"), 
    textvariable=txtinput, 
    width=15, 
    bg="light grey", 
    justify='right'
)
txt.pack(expand=True, fill="both", )
"""
#==================================================================


#1st FARME
br1 = Frame(root, bg="#000000")                 #Black = "#000000"
br1.pack(expand = True, fill = "both",)

b1 = Button(br1, text="1", font=("verdana", 22),  border=0, command=lambda:Clk(1))
b1.pack(side=LEFT, expand=True, fill="both")

b2 = Button(br1, text="2", font=("verdana", 22),  border=0, command=lambda:Clk(2))
b2.pack(side=LEFT, expand=True, fill="both")

b3 = Button(br1, text="3", font=("verdana", 22),  border=0, command=lambda:Clk(3))
b3.pack(side=LEFT, expand=True, fill="both")

bplus = Button(br1, text="+", font=("verdana", 22), border=0, command=lambda:Clk('+'))
bplus.pack(side=LEFT, expand=True, fill="both")

#==================================================================

#2nd FRAME
br2 = Frame(root)                 
br2.pack(expand = True, fill = "both",)

b4 = Button(br2, text="4", font=("verdana", 22),  border=0, command=lambda:Clk(4))
b4.pack(side=LEFT, expand=True, fill="both")

b5 = Button(br2, text="5", font=("verdana", 22),  border=0, command=lambda:Clk(5))
b5.pack(side=LEFT, expand=True, fill="both")

b6 = Button(br2, text="6", font=("verdana", 22),  border=0, command=lambda:Clk(6))
b6.pack(side=LEFT, expand=True, fill="both")

bminus = Button(br2, text="-", font=("verdana", 22),  border=0, command=lambda:Clk('-'))
bminus.pack(side=LEFT, expand=True, fill="both")

#==================================================================

#3rd FRAME
br3 = Frame(root)                 
br3.pack(expand = True, fill = "both",)

b7 = Button(br3, text="7", font=("verdana", 22),  border=0, command=lambda:Clk(7))
b7.pack(side=LEFT, expand=True, fill="both")

b8 = Button(br3, text="8", font=("verdana", 22),  border=0, command=lambda:Clk(8))
b8.pack(side=LEFT, expand=True, fill="both")

b9 = Button(br3, text="9", font=("verdana", 22),  border=0, command=lambda:Clk(9))
b9.pack(side=LEFT, expand=True, fill="both")

bmul = Button(br3, text="*", font=("verdana", 22),  border=0, command=lambda:Clk('*'))
bmul.pack(side=LEFT, expand=True, fill="both")

#==================================================================

#4th FRAME
br4 = Frame(root)                 
br4.pack(expand = True, fill = "both",)

clr = Button(br4, text="C", font=("verdana", 22),  border=0, command=lambda:Clr())
clr.pack(side=LEFT, expand=True, fill="both")

b0 = Button(br4, text="0", font=("verdana", 22),  border=0, command=lambda:Clk(0))
b0.pack(side=LEFT, expand=True, fill="both")

beql = Button(br4, text="=", font=("verdana", 22),  border=0, command=lambda:Eql())
beql.pack(side=LEFT, expand=True, fill="both")

bdiv = Button(br4, text="/", font=("verdana", 22),  border=0, command=lambda:Clk('/'))
bdiv.pack(side=LEFT, expand=True, fill="both")

#==================================================================

root.mainloop()
