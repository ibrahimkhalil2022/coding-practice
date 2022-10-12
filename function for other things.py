

#def swap(x, y):
    #temp = x
    #x = y
    #y = temp

#driver code
#x = 2
#y = 3
#swap(x, y)
#print(x)


###########################

# Python Program to demontrate accessing of
# variables of nested function


def f1():
    s = "Ibrahim Khalil"

    def f2():
        print(s)

    f2()

f1()
