

# This is the example of print simple pyramid pattern
n = int(input("Enter the number of rows: "))

# Outer loop to handel number of rows

for i in range (0, n):
    # inner loop to handel number of columns
    # Values is changing according to outer loop
    for j in range(0, i+1):
        # printing stars
        print("* ", end="")



     #ending line after each row
    print()
