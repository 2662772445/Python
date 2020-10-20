x = 25
def new():
    x = 10
    print('The local variable x is', x)

    def innew():
        global x
        print('The global x inside innew is', x)
        x = x * 4
        print('The updated global x inside innew is', x)

    print('Before calling innew', x)
    print('Calling the function innew')
    innew()
new()
print('x in main', x)
