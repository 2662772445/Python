a = 'Hello, Everyone'

vow = 0

for i in a:
    if i in 'aeiouAEIOU':
        print(i,end=',')
        vow = vow + 1
print(vow)
