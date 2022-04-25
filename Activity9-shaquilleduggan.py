'''Write a function that given a list will print out all the values in that list'''

MyList = [7, 14, 21, 28]

for element in MyList:
    print(element)

# Write a function that takes in one integer as a parameter and will print out your name as many times as specified by the argument.

for i in range(7):
    print("my name is Shaq")



# Create a function that is given a list of numbers as a parameter.

# Sort this list in any way other than using methods from the List object. That means no calling the “.sort()” or “sorted()” method.

# CAN NOT USE the .sort() OR .sorted()

def rearrange(MyList = [37, 1, 26]):
    # Logic for "MyList[0]"
    if(MyList[0] < MyList[1] and MyList[0] < MyList[2]):
        smallestnum = MyList[0]
    elif (MyList[0] > MyList[1] and MyList[0] > MyList[2]):
        greatestnum = MyList[0]
    else:
        middlenum = MyList[0]

   # Logic for "MyList[1]"
    if(MyList[1] < MyList[0] and MyList[1] < MyList[2]):
        smallestnum = MyList[1]
    elif (MyList[1] > MyList[0] and MyList[1] > MyList[2]):
        greatestnum = MyList[1]
    else:
        middlenum = MyList[1]

    # Logic for "MyList[2]"
    if(MyList[2] < MyList[1] and MyList[2] < MyList[0]):
        smallestnum = MyList[2]
    elif (MyList[2] > MyList[1] and MyList[2] > MyList[0]):
        greatestnum = MyList[2]
    else:
        middlenum = MyList[2]

    # Last step
    solution = smallestnum, middlenum, greatestnum
    print(list(solution))
rearrange()


# - Write a function called isSorted which will be passed in a list of numbers

# - Your functions job is to determine if the list is in need of being sorted, or if it already came sorted.

# - Your function should return a boolean determining whether or not that is the case.

def is_it_sorted_or_not(MyList):
    for item in range(0, len(MyList)- 1):
        if(MyList[item] > MyList[item + 1]):
            return False

    return True

The_answer = is_it_sorted_or_not([7, 14, 28])
print(The_answer)

# - Write a function that will be passed a String as a parameter

# - Your functions job is determine whether or not the String passed in is a Palindrome using booleans.
# -True If your word is a palindrome
# -False If you're word is not a Palindrome

def is_it_a_palindrome_or_not(string):
    og_word = list(string)
    print(og_word)

    reverse_word = og_word.copy()
    reverse_word.reverse()

    if(og_word == reverse_word):
        return True
    else:
        return False

The_answer = is_it_a_palindrome_or_not("abjhdsj")
print(The_answer)
