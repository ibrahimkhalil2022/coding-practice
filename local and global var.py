
a = 1
# Uses global because there is no local 'a'
def f():
    print('Inside f() :', a)


#Variable 'a' is redefined as a local
def g():
    a = 2
    print("Inside g() : ", a)


# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)

 # Global scope
print('Global : ', a)
f()
print(' Global : ', a)
g()
print(' Global : ', a)
h()
print(' Global : ', a)
