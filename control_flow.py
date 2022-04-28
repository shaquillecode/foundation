"""Control Flow"""
A = 1000
B = 2000
C = 500

if (A > B and A > C):
    print(" a is the greatest ")

elif(B > A and B > C):
    print(" b is the greatest ")

else:
    print("c is the greatest")

# - Write a Program to imitate a Street light.

GREEN = True
YELLOW = False
RED =  False

if GREEN:
    print("GO")

elif YELLOW:
    print("Slow down")

else:
    print("STOP!!!")


# - Without using any built in String or List methods.
# - (Do not use the .sort() or .sorted() method)
# - Create a function that takes in 3 integers as parameters.
# - Order the numbers from least to greatest.
# - Return these values as a set in a tuple.
# - Check the data type of the value you are returning.
# - Your function assumes that data type.

# When solving a programming problem.
# INPUT PROCESS OUTPUT (IPO)
# What am I given?(Input)
# What needs to be done?(Process)
# What needs to be given back?

def sort_three(num1, num2, num3):
    '''Logic for least to greatest'''
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
    return solution

print(sort_three(2000, 40000, 2))

LENGTH = len(sort_three(2000, 40000, 2))
print(LENGTH)
