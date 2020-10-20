thisdist = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
print(thisdist)

for x in thisdist:
    print(x, end=' ')   
print(' ')

for x in thisdist:
    print(thisdist[x], end=' ')  
print(' ')

for x, y in thisdist.items():
    print(x, '=', y) 
print(' ')
