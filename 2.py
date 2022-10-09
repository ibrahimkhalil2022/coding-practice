#Python program showing how to
# multiple input using split

#Taking two input at a time
x, y = input("Enter two values: ").split()
print("Number of Boys: ", x)
print("Number of girls: ", y)
print()

#Taking three inputat a time
x, y, z = input("Enter three values: ").split()
print("Total numbre if students: ", x)
print("Number of boys: ", y)
print("Number of girls: ", z)
print()

#Taking two inputes at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second numnber is {}".format(a,b))
print()

#taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
