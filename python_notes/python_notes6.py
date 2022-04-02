'''Loops are used for iterating over a sequence'''
#An example of a sequence: Lists, Tuples, Strings, Dictionaries....

people = ["Elvis", "Tyler", "Lydell", "Trey", "Lisandi"]
colors = ("Blue", "Green", "Red", "Yellow", "Pink")

for person in people:
    print("Current Person: ", person)

for color in colors:
    print("Current Color: ", color)

#With for loops think like this:
#for [BLANK] in [BLANK]:
#Where the first [BLANK] is the "counter", and the second [BLANK] is the object.

#Break Keyword:
for person in people:
    if person == "Lydell":
        break
    print("Current person is, ", person)

#Continue Keyword:
# for person in people:
#     if person == "Lydell" or person == "Trey":
#         print("It's supposed to stop right here but it doesn't")
#         continue
#     print("Current Person is, ", person)

#Range Method
#With range(x, y), the first argument is an integer representing where you would like to start
#The second argument is also an integer
#That represents where you would like to stop NON INCLUSIVE meaning
#It'll be one less than the value you pass in.
#Example, if you pass in range(0, 10)
#It'll start at 0, and stop at (one less than 10) which is 9.
for index in range(0, 10):
    print(index, end= ' ')
print()
#if you only pass in one argument into the range() function,
#then it will ASSUME that you want to start from 0.
#The ONE argument is an integer
#that represents where you would like to stop NON INCLUSIVE meaning
#it'll be one less than the value you pass in.
for index in range(9):
    print(index, end= ' ')

print()
#If you pass THREE arguments into the range(x, y, z) function, then...
#The first argument still represents where you want to start INCLUSIVELY
#The second argument still represents where you want to stop EXCLUSIVELY
#The third argument indicates by
#how much you would like to increment your counter by after each iteration of the loop
for index in range(7, 0, -1):
    print(index, end= ' ')

#While Loops execute based on a condition,
#You can change or control the flow of your while loop with
#A flag, or a counter.
print()
CNT = 0

while CNT < 6:
    print(CNT,end= ' ')
    CNT += 1

#The other way is with flags....
print()
#Example:
FLAG = True
NUM = 0
while FLAG:
    if NUM == 5:
        FLAG = False
    else:
        print(NUM,end= ' ')
        NUM += 1

print()
#Nested Loops
#These become super handy when you're
# dealing with matrices... or 2-Dimensional Lists.... OR, a list of lists...

#Nested Loops
li = [["Bitcoin", "Etherium"],["Tesla", "NIO"], ["Elvis", "Shaquille"], ["Blue", "Red"]]

NAME = li[2][1]
print(NAME)
for count, ele in enumerate(li):
#     print(li[i])
    for k in li[count]:
        print(k)

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
#If the number on the left is SMALLER than the number on the right,
# then it will return the number on the
#left..... everytime...
# print(50 % 5)

#Write a function that takes an integer as a
#parameter and print your name out as many times as specified
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
