"""--Create a function named add that expects two arguments"""
# --Return the sum of those two arguments.
# --Repeat this process for Subtracting, Multiplying and Dividing

def addition(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    if num2 != 0:
        return num1 / num2

#Test Cases

print(addition(23, 7))
print(subtraction(37, 7))
print(multiplication(6, 5))
print(division(180, 6))

# Defining a Function in Python

# First thing you have to do:
    #1. KEY WORD: "def"
    #2. FUNCTION NAME: "Call it whatever you want, but make sure it is relevant to the functions' behavior"
    #3. PARENTHESIS: Put after the function name
    #4. COLON:"Put This symbol after paranthesis -> : "
    #5. Optionally: Consider if this function needs a parameter/argument.
    #6. CALL THE FUNCTION: Call the function by its name when you want to execute all the code within it.

def printStuff(name_dict):
    print("fun")
    print("More fun!")
    print("Even more Fun!")
    print("Now I am Chocolate wasted =/")
    print(f"Dictionary = {name_dict}")

printStuff("shaq")

def printStuff2(name):
    print(f"Hi my name is {name}")

printStuff2("fish")

mydict = {
"name": "shaq",
"year" : 2019,
"I am learning" : True}

printStuff(mydict) #This will input mydict value into the printstuff function parameter and run that function.

def printStuff3(mylist):
    print(type(mylist))
    mylist.append("USD")
    mylist.append("is winning now")
    print(mylist)

printStuff3([])

mylist2 = ["shaq", "attack"]

printStuff(mylist2)

def gimmefive():
    return [5] #Function ends at return
    print("Hello")

Yes= gimmefive()
print(Yes)

def gimmefive():
    pass

T= gimmefive()
print(T)   #None value is equivalent to null in other languages and zero but it is still an object.expected outcome
