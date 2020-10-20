x = 50
def foo():
    x = 20
    def bar():
        global x
        x = 30
        print('x inner :', x)

    print('x outer :', x)
    print('Calling bar now')
    bar()
    print('After calling bar :', x)
foo()
print('x outside :', x)
