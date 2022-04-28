"""
Create a function named add that expects two arguments.
Repeat this process for Subtracting, Multiplying and Dividing.
"""
# Defining a Function in Python

# First thing you have to do:
    #1. KEY WORD: "def"
    #2. FUNCTION NAME: "Call it whatever you want, but make sure it is relevant to the functions' behavior"
    #3. PARENTHESIS: Put after the function name
    #4. COLON:"Put This symbol after paranthesis -> : "
    #5. Optionally: Consider if this function needs a parameter/argument.
    #6. CALL THE FUNCTION: Call the function by its name when you want to execute all the code within it.

def addition(num1,num2):
    '''Returns Sum'''
    if isinstance(num1,int) and isinstance(num2, int):
        res = num1 + num2
        return res

def subtraction(num1,num2):
    '''Returns Difference'''
    if isinstance(num1,int) and isinstance(num2, int):
        res = num1 - num2
        return res

def multiplication(num1,num2):
    '''Returns Product'''
    if isinstance(num1,int) and isinstance(num2, int):
        res = num1 * num2
        return res

def division(num1,num2):
    '''Returns Quotient'''
    if isinstance(num1,int) and isinstance(num2, int):
        if num2 != 0:
            res = num1 / num2
            return res

#Test Cases
print(addition(23, 7))
print(subtraction(37, 7))
print(multiplication(6, 5))
print(division(180, 6))

def gimme_five():
    return [5] #Function ends at return
    print("Hello are you ready for a High Five?")

YES = gimme_five()
print(YES)

def gimmeFive():
    pass

NO = gimmeFive()
print(NO)   #None value is equivalent to null in other languages and zero but it is still an object.expected outcome
