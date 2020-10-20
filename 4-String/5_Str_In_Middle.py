s1 = 'ABCDEF'
s2 = 'XYZ'

l = len(s1)
m = int(l/2)

s3 = s1[:m] + s2 + s1[m:]

print(s3)
