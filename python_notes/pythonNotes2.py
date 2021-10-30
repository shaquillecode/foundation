#Strings in python are sorrounded by either single or double quotes
#Concatenation

# name = "Elvis"
# age = 27

# print("My name is " + name + " i am " + str(age) + " years old son")

#In order to change the data type of a variable, specifically an Integer to a String you use: 
#str()
#Inside of this function goes any other data type. The function will automatically convert it into a String
# str(99) -> "99"
# str(True) -> "True"

#String Formatting

#Argument by Position
words = "I want the new {3} but it is priced at {1}".format("Toshiba  TV", 2000.00, "Playstation 5", "Tesla Model X")
print(words)


#.format() is a built in function of the String Object in Python. 


#Argument by Name
words1 = '{} {} {}'.format('a', 'b', 'c')
print(words1)
words2 = "My name is {}".format('ShaQ')
print(words2)

#F-Strings -> After Python 3.6
# name = "Elvis"
# age = 27
# print(f"My name is {name} and my age is {age}")

#String Methods
name = "Elvis"
name2 = "TYLER"
# print(f"Hi my name is {name}")

#Capitalize first letter
# firstLetterCaps = name.capitalize()
# print(firstLetterCaps)

#Capitalize all letters
# upperCaseLetters = name.upper()
# print(upperCaseLetters) -> Returns String all Uppercase

# name = "Elvis"
# name = "Tyler"
# name = "Anthony"

# print(name)

#Lowercase all characters in the String
# lowerCaseLetters = name2.lower()
# print(lowerCaseLetters) -> returns String in all lowercase letters

#Swap lowercase to uppercase and uppercase to lowercase
# swapCases = name.swapcase()
# print(swapCases) -> Swaps lower case letters with uppercase, and vice versa

#Get the length of the String 
# length = len(name)
# print(length) -> Returns an Integers of the Length of the String

#Replace a String with another String 
# s = "Hi My name is Elvis and is teaching"
# newString = s.replace("is", "isn't")
# print(newString)