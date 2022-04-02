'''
import example

print(example.add(4, 9))
print(example.mult(4, 9))
print(example.sub(5, 4))
print(example.div(10, 2))
'''
import random

#Modules:
#A module is basically a file containing a set of functions to include in your application.
#There are CORE python modules,
#Which are modules that you can install using the "pip" package manager
#(which includes Django!) as well as any other custom pip package
#pip stands for "(P)ython (I)nstall (P)ackages"

# Core Modules
# Keyword: import
# Module 1: datetime
import datetime

# Keyword: import
# Module 2: time
import time

currentDate = datetime.datetime.now()
print(currentDate)
print(f"You are currently in the year: {currentDate.year}")
print(f"You are currently in the {currentDate.day} day of your month")
print(currentDate.month)
print(currentDate.hour)
print(currentDate.minute)
print(currentDate.second)
print(time.time())


#pip modules
#CamelCase is a pip module.
# pip packages are not by default available in Python
#So for the most part, when you want to work with modules that are custom, you probably
#will have to first install it using pip.

#To check if you have pip: Go to the command terminal, and type the command: "pip --version"
#If you do not have pip installed then you can install it with this command:
#"python -m pip --version"

#After you have installed pip, run the "pip3 freeze"

#Run a virtual environmrnt first
#To install a custom package like Django, run the command "pip3 install django"

#When you finish running that command, run the "pip3 freeze" again,

#Install another package called camelcase
#Keyword: pip3
#Package: camelcase
#Solution: pip3 install camelcase

# import camelcase

# camel = camelcase.CamelCase()
# #camelcase has a method called hump, you pass in text and it will display it in camcelcase
# name = "elvis garcia"
# print(camel.hump(name))


#==============================================================================#

#Random has a module called "getrandbits()"
#Returns a random number between 0 up to whatever max value you can get with the bits passed in...
#If I pass in 4 bits, then the maximum value is 15
#That means that if you passed in 4 as an argument,
#It would generate random numbers between 0 and 15 (inclusive)



randomNumber = random.getrandbits(4)


#Test and Print the value of that random number
print(randomNumber)


# Generating Random Lists

#Generate a random number using DECIMAL VALUES instead of BINARY
#The method is "randrange(x, y)"

#The first parameter "x" indicates where you want to start
#The second parameter "y" indicates where you want to end (exclusive)

randNum = random.randrange(0, 10)
print(randNum)


# "randint()" This function returns a number between the given range that you specify
# The second argument is inclusive.
#So with randrange(x, y) -> Gets random number between x and y-1
#With randint(x, y) -> Gets random number between x and y


randNum2 = random.randint(0,10)
print(randNum2)
