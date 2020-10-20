
# if file is in different location then use above
#f = open("E:\College\Python\\7-Files\\regex_sum.txt", "r")

# 1 Through (f.read)
f = open("regex_sum.txt", "r")
print(f.read())
f.close()

# 2 Through loop
f = open("regex_sum.txt", "r")
for x in f:
    print(x)
