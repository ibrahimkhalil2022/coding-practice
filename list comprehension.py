#python Program Showing
#how to take multiple input
#using List Comprehension

#taking two inpt at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is: ", x)
print("Second number is: ", y)
print()

#taking three input at a time
a, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First number is: ", x)
print("Second number is: ", y)
print("third number is: ", z)
print()

#taking two inputs at a time
x, y = [int(x) for x in input("Enter teo values: ").split()]
print("First number is {} and second number is{}".format(x, y))
print()

#taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x)
