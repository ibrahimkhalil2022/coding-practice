#python program to demonstrate neted ternary operator
a = 10
b = 20

#Copy value of a in min if a < b else copy b
#min = a if a < b else b

#print(min)
#########################################

#print("Both a and b are equal" if a ==b else "a is greater than b" if a >b else "b is grater than a")

#######################################

#Use tuple for selecting an item
# (if_test_false, if_test_true)[test]
# if[a < b] is true it return 1, so element with 1 index will print
#else id [a<b] is false it return 0, so element with 0 index will print
#print((b,a) [a<b])

#Use Dictionary for selecting an item
#if [a < b] is true then value of true key will print
# else if [a < b] is false then value of False key will print
#print({True: a, False: b} [a < b])

#lamda is more efficient then above two methods
#because in lamda we are assure thet
# only one expression will be evaluated unlike in
#tuple and Dictiionary

#print((lambda: b, lambda: a)[a < b]())

###################################

if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")
