
a1 = [1, 2, 2, 3, 4, 10, 9, 11, 8, 7, 6, 3, 11, 9, 3, 1, 3]

print(len(a1))

a2 = []
for i in a1:
    if i in a2:
        continue
    elif i not in a2:
        a2.append(i)
print(a2)
print('')

for j in a2:
    print('{} Repeated : {}'.format(j,a1.count(j)))
