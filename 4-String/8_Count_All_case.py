a = 'f1g4h4&^$fb5u4b44g$^%&'

ch = []
no = []
sm = []

char = 0
num = 0
sym = 0

for i in a:
    if i.islower() or i.isupper():
        ch.append(i)
        char = char + 1
    elif i.isnumeric():
        no.append(i)
        num = num + 1
    else:
        sm.append(i)
        sym = sym + 1

str1 = ''.join(ch + no + sm)
print(str1)

print('Count character case :',char)
print('Count digits case :',num)
print('Count symbol :',sym)
