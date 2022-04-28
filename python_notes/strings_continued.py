'''Strings continued'''

#Concatenation
NAME = "Shaq"
AGE = 28

print("My Name is " + NAME + " I am " + str(AGE) + " years old shunnnn!")

#In order to change the data type of a variable, specifically an Integer to a String you use:
str()
#The function will automatically convert it into a String
# str(99) => "99"
# str(True) => "True"

#String Formatting

#Argument by WORD
WORD = " The new {2} is priced at {1} as of {0}".format("March 2022", 114990, "Tesla Model X")
print(WORD)

#.format() is a built in function of the String Object in Python.

#Argument by NAME
WORD_NAME = '{} {} {}'.format('Argument', 'by', 'Name')
print(WORD_NAME)

#F-Strings -> After Python 3.6
NAME = "shaq"
AGE = 28
print(f"My Name is {NAME} and my Age is {AGE}")

#String Methods

#Capitalize first letter
CAPS = NAME.capitalize()
print(CAPS)

#Capitalize all letters
UPPER = NAME.upper()
print(UPPER) # => Returns String all Uppercase

#Lowercase all characters in the String
LOWER = UPPER.lower()
print(LOWER) # => returns String in all lowercase letters

#Swap lowercase to uppercase and uppercase to lowercase
SWAP = NAME.swapcase()
print(SWAP) # => Swaps lower case letters with uppercase, and vice versa

#Get the LENGTH of the String
LENGTH = len(NAME)
print(LENGTH) # => Returns an Integers of the LENGTH of the String

#Replace a String with another String
SENTENCE = "Hi My Name isn't SHAQ and I am not learning "
NEW_STRING = SENTENCE.replace("isn't", "is").replace('not','')
print(NEW_STRING)
