#A list is a collection which is ordered and mutable, (meaning it can be modified directly.)
#A list can contain dulicate values -> ["Elvis", "Elvis", "Tyler"]

#Create a list
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

#The following is going to be referenced in future courses
#Creating a List using a Constructor: (Sneak Peak to OOP)
# numbers = list((1, 2, 3, 4, 5))
# print(numbers)

#Accessing an Element in a List
# fruits = ["Orange", "Apples", "Mangos", "Pineapples", "Grapes", "Soursop", "Kiwi", "Starfruit"]
#             #0         #1        #2         #3           #4         #5        #6        #7
#             #-8       #-7       #-6        #-5          #-4        #-3       #-2       #-1
#if I want orange:
# a = fruits[0]
# b = fruits[-8]

#Get the value, you print out the location of where you referenced the value that you want:
# print(b)

#Get the Length of a List: 
# length = len(fruits) #This will return to you the length of the List
# print(length) #Length returns an Integer. This will become useful especially when we begin using Loops and Conditionals
words = "elvis"

# #Lisandi Question: 
# print(str(len(words)).upper())
# #End of Lisandi Question

#Appending to a List

#Don't Do this: 
# fruits += "DragonFruit"
# print(fruits)

#Do this:
# fruits.append("DragonFruit")
# print(fruits)
#Objects DOT Functionality
#You reference the Object FIRST
#Then you reference the Objects Functions

#Removing from a List: 

# fruits = ["Orange", "Apples", "Mangos", "Pineapples", "Grapes", "Soursop", "Kiwi", "Starfruit", "Pears", "Watermelon"]
#             #0         #1        #2         #3           #4         #5        #6        #7
            
# fruits.remove("Grapes")
# print(fruits)

#Popping from a List: 
fruits = ["Orange", "Apples", "Mangos", "Pineapples", "Grapes", "Soursop", "Kiwi", "Starfruit", "Pears", "Watermelon"]
            #0         #1        #2         #3           #4         #5        #6        #7
            

# fruits.pop(6)
# fruits.pop(3)
# print(fruits)
#This is nothing than another way to remove an element from a list
#The only difference, is that you are referencing an index position as opposed to the value itself.


#Reversing a List: 
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)


#Sorting A List: 
fruits.sort(reverse=True) #In this line, the object has been modified
print(fruits) #You can just print the object itself
print("Before being sorted: " + str(fruits))

# fruits.sort()
# print(fruits)


# print("After being sorted: " + str(fruits))
#Null/None is the absence of an object. But it itself is still an object
#Kind of like how 0 is the absence of value in numbers, but is still a number.


fruits[0] = "Tomatoes"
print(fruits)