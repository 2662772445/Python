from tkinter import *

#============================================================================================

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

#============================================================================================

root = Tk()
root.title("Calculator")

txtinput = StringVar()


#============================================================================================

txt = Entry(
    root, 
    font=('arial', 15), 
    textvariable=txtinput, 
    bd=6, 
    width=15,
    bg="light grey", 
    justify='left'
)
txt.grid(columnspan=4)

#============================================================================================

b7 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="7", command=lambda:Clk(7))
b7.grid(row=1, column=0)

b8 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="8", command=lambda:Clk(8))
b8.grid(row=1, column=1)

b9 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="9", command=lambda:Clk(9))
b9.grid(row=1, column=2)

add = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="+", command=lambda:Clk('+'))
add.grid(row=1, column=3)

#============================================================================================

b4 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="4", command=lambda:Clk(4))
b4.grid(row=2, column=0)

b5 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="5", command=lambda:Clk(5))
b5.grid(row=2, column=1)

b6 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="6", command=lambda:Clk(6))
b6.grid(row=2, column=2)

sub = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="--", command=lambda:Clk('-'))
sub.grid(row=2, column=3)

#============================================================================================

b1 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="1", command=lambda:Clk(1))
b1.grid(row=3, column=0)
b2 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="2", command=lambda:Clk(2))
b2.grid(row=3, column=1)

b3 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="3", command=lambda:Clk(3))
b3.grid(row=3, column=2)

mul = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="x", command=lambda:Clk('*'))
mul.grid(row=3, column=3)

#============================================================================================

b0 = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="0", command=lambda:Clk(0))
b0.grid(row=4, column=0)

clear = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="C", command=Clr)
clear.grid(row=4, column=1)

equal = Button(root, padx=10, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="=", command=Eql)
equal.grid(row=4, column=2)

div = Button(root, padx=11, pady=10, bd=4, bg="grey", fg="black", font=('arial', 10, 'bold'), 
            text="/", command=lambda:Clk('/'))
div.grid(row=4, column=3)

#============================================================================================


root.mainloop()
