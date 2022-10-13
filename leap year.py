

#default function to implement conditions to check leap year

def CheckLeap(Year):
    #checking if the given year is leap year

    if ((Year % 400 == 0)or
         (Year % 100 != 0) and
        (Year % 4 == 0)):

        print("Given Year is leap Year");

        # elseit is not a leap year

    else:
        print("Given year is not a leap year")



Year = int(input("Enter the number: "))

# Printing result

CheckLeap(Year)
