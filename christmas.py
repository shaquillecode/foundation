'''While loops'''

# Create a While loop that goes through the 12 days of Christmas:
# Solution 1
INDEX = 0
DAY = 1
theTruestLoveofmywholelifeGifts = ["  a Love bird", " a Lion", " a Liger",
" a Black panther", " a Elephant", " a Baby Goat", " a Giraffe", " a Silverback Gorilla",
" an Anaconda", " a HoneyBadger", " a Pitbull", " a Parrot"]

while DAY < 13:
    print(f"On the {DAY} of Christmas,\
    my true love gave to me{theTruestLoveofmywholelifeGifts [INDEX]}")
    DAY = DAY + 1
    INDEX = INDEX +1

# Create a While loop that takes a list of integers, and gives the SUM of the integers
# Solution 2

_SUM = 0
i = 0

Thelist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

while i < len(Thelist):
    _SUM += Thelist[i]
    i = i + 1

print(_SUM)

# For Loops
# 1. 12 days of Christmas using For Loops

for INDEX in range(1,13):
    print(f" On the {INDEX} of christmas my true love gave to me!")

# 2. Referencing a list of any size contaning numbers,
# return the SUM of all those numbers in the List

MyList = [7, 14, 21, 28]
SUM1 = 0
SUM2 = 0

for listItem in MyList:
    SUM1 += listItem

# Using The Range Method
for listIndex,listItem in enumerate(MyList):
    SUM2 += MyList[listIndex]


print(SUM1)
print(SUM2)
