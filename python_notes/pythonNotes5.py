#assignment 8
#You creating the function
def sum(num1, num2):
    return num1 + num2


x = 1000000
y = 0
print(x - y)
solution = sum(15, 15)
print(solution)
#You passing in arguments into the function
sum(7654382736, 987536243)

#printing the expected result of your function
#wrap your function name and its arguments, INSIDE of a print function
print(sum(7654382736, 987536243))

#You will be working with data PASSED IN by the user
#You will have NO idea what that value is before hand
#So you use a variable to represent that value as a placeholder, and then 
#just perform operations on those variables that represent the values that you
#originally did not know.

#Create a function
#Think the keyword "def"

#Now do this for Subtraction, Multiplication, and Division

#NOTES ON FUNCTIONS:
#A function is a block of code which only runs when it is called. 
#For example, you made the function called sum, and then called it to see the value.
#In Python, we do not use parenthesis or curly brackets to indicate that we are entering our body of code.
#In Python, we simply indent after a colon and make a new line. 
#The colon sign is -> :

#Create a function: 
#first, use the "def" keyword
#Then follow with a function name 
#Then follow with parentheses
#Then follow with a colon
#Determine if you need parameters
#If you do, place them inside of your functions' parentheses
def sayHello():
    print("Welcome to my website, I want you to experience the best of the best of the best.")

sayHello()

#Another way you can do this, is by assigning a default value to a parameter
def sayHello(name = "Elvis"):
    print(f"Hi my name is {name}")

sayHello()
sayHello("Tyler")

#Returning Values
#IPO - Input, Process, Output

def getSum(num1 = 0, num2 = 0):
    return num1 + num2

#You can prove the data type by using the type()
#Version 1
# solution = getSum()
# print(type(solution))

#Version 2
# print(type(getSum()))

#Function Example: 
def AddOne(num):
    return num + 1

print(AddOne(3))


    