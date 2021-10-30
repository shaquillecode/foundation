#A for Loop is used for iterating over a sequence
#An example of a sequence: Lists, Tuples, Strings, Dictionaries....

people = ["Elvis", "Tyler", "Lydell", "Trey", "Lisandi"]
colors = ("Blue", "Green", "Red", "Yellow", "Pink")

# for person in people:
#         print("Current Person: ", person)

# for color in colors:
#         print("Current Color: ", color)

#With for loops think like this: 
#for [BLANK] in [BLANK]:
#Where the first [BLANK] is the "counter", and the second [BLANK] is the object.

#Break Keyword:
# for person in people:
#         if(person == "Lydell"):
#                 break
#         print("Current person is, ", person)

#Continue Keyword: 
# for person in people: 
#         if(person == "Lydell" or person == "Trey"):
#                 print("It's supposed to stop right here but it doesn't")
#                 continue
#         print("Current Person is, ", person)

#Range Method
#With range(x, y), the first argument is an integer representing where you would like to start
#The second argument is also an integer that represents where you would like to stop NON INCLUSIVE meaning
#it'll be one less than the value you pass in. 
#Example, if you pass in range(0, 10) -> It'll start at 0, and stop at (one less than 10) which is 9.
# for index in range(0, 10):
#         print(index)

#if you only pass in one argument into the range() function, then it will ASSUME that you want to start 
#from 0. 
#The ONE argument is an integer that represents where you would like to stop NON INCLUSIVE meaning
#it'll be one less than the value you pass in.
# for index in range(10):
#         print(index)


#If you pass THREE arguments into the range(x, y, z) function, then...
#The first argument still represents where you want to start INCLUSIVELY
#The second arguement still represents where you want to stop EXCLUSIVELY
#The third argument indicates by how much you would like to increment your counter by after each iteration
#of the loop
# for index in range(10, 0, -1):
#         print(index)

#While Loops execute based on a condition, and you can change or control the flow of your while loop with 
#a flag, or a counter. 

# counter = 0

# while(counter < 10):
#         print(counter)
#         counter += 1

#The other way is with flags....

#Example:
# flag = True
# num = 0
# while(flag):
#         if(num == 5):
#             flag = False
#         else:
#             print(num)
#             num += 1

#Nested Loops
#These become super handy when you're dealing with matrices... or 2-Dimensional Lists.... OR, a list of lists...





#Nested Loops
li = [["Bitcoin", "Etherium"],["Tesla", "NIO"], ["Elvis", "Tyler"], ["Blue", "Red"]]

# name = li[2][1]
# print(name)
# for i in li: 
#     for k in li[i]: 
#         print(li[i][david])

L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]     

# print(list) 
# for list in L:
#     print(list, end=' ')
#     for number in list:
#         print(number, end=' ')

#The modulus operator is a conditional operator, that is denoted with a "%":
#It's function: It divides two numbers, and returns the remainder.
#More Specifically: x % y -> Divide X by Y and return what is leftover, NOT the result...
#Another Property of the Modulus Operator is: 
#If the number on the left is SMALLER than the number on the right, then it will return the number on the
#left..... everytime...
# print(50 % 5)

#Write a function that takes an integer as a parameter and print your name out as many times as specified 
#by the argument

# def printNameAlot(num):
#         for i in range(num):
#                 print(f"Elvis Garcia for the {i+1} time ... ")

# printNameAlot(1000)

# def printNameAlot2(num):
#         counter = 0
#         while(counter < num):
#                 print(f"Elvis Garcia for the {counter+1} time ... ")
#                 counter += 1

# printNameAlot2(10)

def printList(dataset):
        for i in dataset: 
                print(i)

def printList2(dataset):
        for i in range(len(dataset)):
                print(dataset[i])

# printList(["Yo", "Whats", "Up", 5, 10])
printList2(["Yo", "Whats", "Up", 5, 10])




