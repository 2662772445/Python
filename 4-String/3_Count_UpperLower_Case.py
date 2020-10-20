a = 'Hey, there how are you, Hope You Are DOING OK'

up = 0
low = 0

print(ord('A'))

for i in a:
    s = ord(i)
    if s >= 65 and s <= 90:
        up = up + 1
    if s >= 97 and s <= 122:
        low = low + 1

print(a)

print(up)
print(low)


'''
a = 'Hey, there how are you, Hope You Are DOING OK'

up = 0
low = 0


for i in a:
    s = ord(i)
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        up = up + 1
    if i in 'abcdefghijklmnopqrstuvwxyz':
        low = low + 1

print(up)
print(low)
'''

