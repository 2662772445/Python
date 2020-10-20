f = open("test.txt", "w")
print(f.write("Hey there, how are you?"))
f.close()

f = open("test.txt", "r")
print(f.read())
