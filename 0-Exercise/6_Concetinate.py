
slist = ['p', 'q']
sout = []

for i in range(1, 6):
    for j in range(0, 2):
        s1 = slist[j]
        s2 = str(i)
        s = s1 + s2
        sout.append(s)

print(sout)


'''
slist = ['p', 'q']

for i in range(1, 6):
    print('p{} q{}'.format(i,i), end=", ")
'''
