a = 'MsUaLhTiAlNI'

low = []
up = []

for i in a:
    if i.islower():
        low.append(i)
    else:
        up.append(i)

str = low + up
str1 = ''.join(low + up)

print(str)
print(str1)
