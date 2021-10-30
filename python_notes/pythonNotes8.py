#Activity 8
'''
import example


print(example.add(4, 9))
# print(example.mult(4, 9))
# print(example.sub(5, 4))
# print(example.div(10, 2))
'''

#Python Notes 8:
#Modules:
#A module is basically a file containing a set of functions to include in your application. 
#There are CORE python modules, which are modules that you can install using the "pip" package manager (which even includes Django!) as well as any other custom pip package
#pip stands for "(P)ython (I)nstall (P)ackages"

# Core Modules
# Keyword: import
# Module 1: datetime
import datetime

# Keyword: import
# Module 2: time
# import time

currentDate = datetime.datetime.now()
# print(currentDate)
# print(f"You are currently in the year: {currentDate.year}")
# print(f"You are currently in the {currentDate.day} day of your month")
# print(currentDate.month)
# print(currentDate.hour)
# print(currentDate.minute)
# print(currentDate.second)


#pip modules
#CamelCase is a pip module. pip packages are not by default available in Python
#but you can install them. Hence pip standing for "Python Install Packages"
#So for the most part, when you want to work with modules that are custom, you probably
#will have to first install it using pip.

#To check if you have pip: Go to the command terminal, and type the command: "pip --version"
#If you do not have pip installed then you can install it with this command: 
#"python -m pip --version"

#After you have installed pip, run the "pip3 freeze"  


#To install a custom package like Django, run the command "pip3 install django"

#When you finish running that command, run the "pip3 freeze" again, and see if it has updated... (it should have...)

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

#Python has a built in module called Random......
#That means, that I do not have to use pip to install Random, because it's part of the CORE package...

#The random module has a set of methods that we are going to be working with today. 

#So let's stick to the basics, we know that to use a module we MUST use the keyword "import" followed by the module that we want to use... like datetime, or camelcase above...

#Now that I mentioned that random has methods, let's practice with some of those methods...

#Let's start with one that will bring us back to our "What is Data?" lesson from Class 1 or Class 2....

#Do not froget that with modules, in order to reference their methods, you simply call it as follows:
'''
module.method()

OR BETTER YET....

<module-name>.<entity-name>

'''

#Random has a module called "getrandbits()"
#It's pretty cool, it will return a random number between 0 up to whatever max value you can get with the bits you passed in...

#So for example, if I pass in 4 bits, then what's the maximum value -> 15
#That means that if you passed in 4 as an argument, it would generate random numbers between 0 and 15 (inclusive)

#Here is an example:
#1. Import the Module: Module Name in this is "random"

import random


#2. Create a variable and store the value of what you get from calling "getrandbit(x)"
#Think about "module.method()"
'''
randomNumber = random.getrandbits(4)
'''

#Test and Print the value of that random number
'''
print(randomNumber)
'''


#Activity 11: Generating Random Lists
'''

Write a function that will take in an integer as a parameter, and will create a list of the size passed in as an argument. I also want you to populate that whole list with random numbers between 0-1023. You're going to be using the getrandbits() method of the random module, so think about how to arrive at that outcome.

#Example I/O
Input -> 5
Output -> [x, y, z, a, b]

'''

#Problem/Notes
'''
Let's say that we want to generate a random number. BUT we don't want to represent the range by the amount of bits. We want to EXPLICITLY input a range using DECIMAL VALUES instead of BINARY. 

The method that can help you with this is called "randrange(x, y)"

The method above, takes two parameters (denoted by "x" and "y"). 

#The first parameter "x" indicates where you want to start
#The second parameter "y" indicates where you want to end (exclusive)

#So for example, if we have "randrange(x, y)" and we subtitute "x" with the value 0, and "y" with the value of 10, then we will have a function that will generate a random number from 0-9.

This should remind you A WHOLE LOT (it even contains the word itself) of the "range()" function in the loops....

#The only difference, it will return a random number within the range, not iterate through a sequence of elements. 
'''

#Let's try it: 
# randNum = random.randrange(0, 10)
# print(randNum)

#Activity 11.1: Working with RandRange
'''
Similar to the previous problem, I want you to create a function that will generate a random list and takes in a number as a parameter that will be the size of the list. BUT I want the values passed in to range between 20 and 78 specifically exclusive of the 78.

#Step 1: Write the function name and make sure it has a parameter place holder that will represent an Integer in your function
#Step 2: Make a new list
#Step 3: Make that list the size of the paramter/argument passed in
#Step 4: 
#Step 5: Return the List
'''

#Moving on from "randrange()" there is also a function in the random module called "randint()".

#This function returns a number between the given range that you specify BUT it IS inclusive of you indicate you want it to end: 

#This means, that the only real difference between this and randrange is that the second argument is inclusive. 
#So with randrange(x, y) -> Gets random number between x and y-1
#With randint(x, y) -> Gets random number between x and y

#Here is an example: 
# randNum2 = random.randint(0,10)
# print(randNum2)

#Activity 11.2: RPS
'''
- Create a function that plays rock paper scissors with you....
- You are to ask the user for INPUT
- If the user inputs "Rock" -> "Scissors" will lose, and "Paper" will win
- If the user inputs "Paper" -> "Rock" will lose, and "Scissor" will win
- If the user inputs "Scissors" -> "Paper" will lose, and "Rock" will win

#HINT
- How can I make the computer make a RANDOM choice between those.... Then maybe compare that computers choice to the user input.... 
- Since the computers choice can be three different values, what I can you use to store a sequence of values
- 3 values is 3 values, do you know a way to generate a random number between 0 and 3? Will it be inclusive of the 3? 



'''

word1 = "Elvis"
word2 = "Tyler"

# print(word1 > word2)