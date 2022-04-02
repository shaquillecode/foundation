'''Creating the function'''
#Returning Values
#IPO - Input, Process, Output
def get_sum(num1, num2):
    '''RETURNS SUM'''
    return num1 + num2

X = 1000000
Y = 0
print(X - Y)

SOLUTION = get_sum(15, 15)
print(SOLUTION)
#You passing in arguments into the function
get_sum(7654382736, 987536243)

#printing the expected result of your function
#wrap your function name and its arguments, INSIDE of a print function
print(get_sum(7654382736, 987536243))

#I will be working with data PASSED IN by the user
#I will have NO idea what that value is before hand
#So I will use a variable to represent that value as a placeholder, and then
#just perform operations on those variables that represent the values

#NOTES ON FUNCTIONS:
#A function is a block of code which only runs when it is called.
#For example, you made the function called get_sum, and then called it to see the value.
#In Python, we do not use parenthesis or curly brackets
# to indicate that we are entering our body of code.
#In Python, we simply indent after a colon and make a new line.
#The colon sign is -> :

#Create a function:
#first, use the "def" keyword
#Then follow with a function name
#Then follow with parentheses
#Then follow with a colon
#Determine if you need parameters
#If you do, place them inside of your functions' parentheses


#Assigning a default value to a parameter
def say_hello(name = "Shaquille"):
    '''Prints Sentence'''
    print(f"Hi my name is {name}")

say_hello()
say_hello("Shaquille O'neal")
