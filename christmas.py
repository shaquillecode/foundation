# While loops

# Create a While loop that goes through the 12 days of Christmas:
# Solution 1
index = 0
day = 1
TheTruestLoveofmywholelifeGifts = ["  a Love bird", " a Lion", " a Liger", " a Black panther", " a Elephant", " a Baby Goat", " a Giraffe", " a Silverback Gorilla", " an Anaconda", " a HoneyBadger", " a Pitbull", " a Parrot"]

while(day < 13):
    print(f"On the {day} of Christmas, my true love gave to me{TheTruestLoveofmywholelifeGifts [index]}")
    day = day + 1
    index = index +1
    
# Solution 2
# Create a While loop that takes a list of integers, and gives the sum of the integers

sum = 0
i = 0

Thelist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

while(i < len(Thelist)):
    sum += Thelist[i]
    i = i + 1

print(sum)

# For Loops
# 1. 12 days of Christmas using For Loops

for index in range(1,13):
    print(f" On the {index} of christmas my true love gave to me!")


# 2. Referencing a list of any size contaning numbers, return the sum of all those numbers in the List

MyList = [7, 14, 21, 28]
sum1 = 0
sum2 = 0

for listItem in MyList:
    sum1 += listItem
    
# Using The Range Method
for listItem in range(0, len(MyList)):
    sum2 += MyList[listItem]


print(sum1)
print(sum2)