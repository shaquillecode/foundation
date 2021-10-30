# num = 5
# while( num == 5):
#      print(" It is me number 5 forever .... ")
#  See above for an infinite loop. Be careful and stop it because it uses up your memory space 

j = 0

while(j < 15):
    print( f"I'm in a while loop and it has run {j + 1} amount of times thus far." )

    j = j + 1 

 # Create a While loop that takes a list of integers, and gives the sum of the integers

sum2 = 0
k = 0

Thelist = [2, 4, 6, 8]
length = len(Thelist)

while(k < length):
    sum2 = sum2 + Thelist[k]
    k = k + 1

print(sum2)

# Declaring Foor loops
#  In general, a for loop has 3 components in the declaration.
    # Component 1: Initializing the Index/Counter
    # Component 2: Creating the Condition
    # Component 3: Incrementation

for index in range(1,13):
    print(f" On the {index}")

# Referencing a list of any size contaning numbers, return the sum of all those numbers in the List

MyList = [7, 14, 21, 28]
sum3 = 0
sum4 = 0
# For loop 
for listItem in MyList:
    sum3 = sum3 + listItem
    
# Using The Range Method
length = len(MyList)
for listItem in range(0, length):
    sum4 = sum4 + MyList[listItem]


for counter in range(1,11,3):
    print(f"I am using iteration number: {counter}")


print(sum3)
print(sum4)