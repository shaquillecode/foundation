'''A list is a collection which is ordered and mutable'''


#Create a list
numbers = [1, 2, 3, 4, 5]
print(numbers)


#Creating a List using a Constructor:
numbers = list((1, 2, 3, 4, 5))
print(numbers)

#Reversing a List:
numbers.reverse()
print(numbers)

#Accessing an Element in a List
fruits = ["Orange", "Apples", "Mangos", "Pineapples", "Grapes", "Soursop", "Kiwi", "Starfruit"]
            #0         #1        #2         #3           #4         #5        #6        #7
            #-8       #-7       #-6        #-5          #-4        #-3       #-2       #-1
#if I want orange:
# a = fruits[0]
# b = fruits[-8]

#Get the value, you print out the location of where you referenced the value that you want:
# print(b)

#Get the Length of a List:
LENGTH = len(fruits) #This will return to you the length of the List
print(LENGTH) #Length returns an Integer.


#Appending to a List
fruits.append("DragonFruit")
print(fruits)

#Objects DOT Functionality
#You reference the Object FIRST
#Then you reference the Object's Functions

#Removing from a List:
fruits.remove("Grapes")
print(fruits)

#Popping from a List:
fruits.pop(6)
fruits.pop(3)
print(fruits)
#Another way to remove an element from a list
#pop is referencing an index position as opposed to the value itself.


#Sorting A List:
fruits.sort(reverse=True) #In this line, the object has been modified
print(fruits) #You can just print the object itself
print("Before being sorted: " + str(fruits))

fruits.sort()

print("After being sorted: " + str(fruits))
#Null/None is the absence of an object. But it itself is still an object
#Kind of like how 0 is the absence of value in numbers, but is still a number.


fruits[0] = "Tomatoes"
print(fruits)
