f = open("E:\College\Python\\7-Files\\test1.txt", "w+")
f.write("Hello World For now, our primary motivation is not to make money or please end users, but instead for us to be more productive in handling the data and information that we will encounter in our lives.When you first start, you will be both the programmer and the end user of your programs.  As you gain skill as a programmer and programming feels more creative to you, your thoughts may turn toward developing programs for others.")
f.close()

f = open("E:\College\Python\\7-Files\\test1.txt", "r")
print(f.read())
f.close
