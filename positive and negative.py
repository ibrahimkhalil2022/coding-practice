
# default function to run if else condition

def NumberCheck(a):
    #Checking if the numeber is positive
    if a > 0:
        print("number given by you is positive!")

    # Checking if the number is negative
    elif a < 0:
        print("Number given by you is Negative")

    # Else the number is zero

    else:
        print("Number given by you is zero")

#taking numner from user

a = float(input("Enter a number as input value: "))
#Printing result

NumberCheck(a)
    
