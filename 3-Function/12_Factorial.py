def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


no = 4
print('Factorial of', no, 'is', fact(no))
