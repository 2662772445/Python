s1 = "ABC"
s2 = "abc"

l1 = len(s1)
print(l1)
m1 = int(l1/2)

l2 = len(s2)
print(l2)
m2 = int(l2/2)

str1 = s1[:1]+s2[l2-1:] + s1[m1:m1+1]+s2[m2:m2+1] + s1[l1-1:]+s2[:1]
print(str1)
