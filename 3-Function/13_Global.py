x = 50
def foo():
    x = 20
    def bar():
        global x
        x = 30
        print('x inner :', x)

    print('x outer :', x)
    bar()
    print('x inside :', x)
foo()
print('x outside :', x)
