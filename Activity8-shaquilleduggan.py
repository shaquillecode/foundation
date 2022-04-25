"""Write a Program to check the greatest among 3 numbers."""
a = 1000
b = 2000
c = 500

if (a > b and a > c):
    print(" a is the greatest ")

elif(b > a and b >c):
    print(" b is the greatest ")

else:
    print("c is the greatest")

# -Write a Program to imitate a Street light.
Green = True
Yellow = False
Red =  False

if Green:
    print("GO")

elif Yellow:
    print("Slow down")

else:
    print("STOP!!!")


# - Without using any built in String or List methods.
# (Do not use the .sort() or .sorted() method)
# Create a function that takes in 3 integers as parameters. Perform some operations that will compare these values and order the numbers from least to greatest.
# - Return these values as a set in a tuple.
# - Remember to check the data type of the value you are returning. Your function assumes that data type.

# Whenever you are solving a programming problem. Think about IPO.
# Not Initial public offering, which is where companies sell shares for cheap.
# INPUT PROCESS OUTPUT
# What am I given?(Input)
# What needs to be done?(Process)
# What needs to be given back?


def SortThree(num1, num2, num3):
    # Logic for least to greatest
    smallestnum = 0
    middlenum = 0
    greatestnum = 0

     # Logic for "num 1"
    if(num1 < num2 and num1 < num3):
        smallestnum = num1
    elif (num1 > num2 and num1 > num3):
        greatestnum = num1
    else:
        middlenum = num1

   # Logic for "num 2"
    if(num2 < num1 and num2 < num3):
        smallestnum = num2
    elif (num2 > num1 and num2 > num3):
        greatestnum = num2
    else:
        middlenum = num2

   # Logic for "num 3"
    if(num3 < num1 and num3 < num2):
        smallestnum = num3
    elif (num3 > num1 and num3 > num2):
        greatestnum = num3
    else:
        middlenum = num3

    # Last step: I just have to organize my solution into a Tuple and return that Tuple

    solution = (smallestnum, middlenum, greatestnum)

    print(type(solution))
    return(solution)

print(SortThree(2000, 40000, 2))

length = len(SortThree(2000, 40000, 2))
print(length)
