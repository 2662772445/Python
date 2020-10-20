str1 = 'abcXYZabc'

l = len(str1)
print(l)
print(str1)

def mname(str1):
    m1 = int(l/2)    # 9/2 = 4.5 = 4   
    m2 = str1[m1-1 : m1+2]
    print(m2)

mname(str1)


'''
str1 = 'abcXYZabc'

l = len(str1)
print(l)
m = int(l/2)
print(str1[m-1 : m+2])
'''
