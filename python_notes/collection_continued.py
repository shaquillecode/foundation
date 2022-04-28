''' Lists, Tuples and Dictionaries'''
#Empty Square Brackets.
myList = []
print(myList)

#When declaring an empty Tuple. You cannot do it the same way as with Lists
# Include a trailing comma at the end of the first element
# myTuple = ("Tank",) -> IS a Tuple
# myTuple2 = ("Tank") -> IS NOT a Tuple


myTuple = ("Tank", "Tone", "Top", "Jim", "Acorns", "Baseball")
myTuple2 = (4, 3, 6, 7, 1)
print(myTuple,type(myTuple))
# type(myTuple) -> Returns the Object Type of that Value


#To delete a tuple, use the keyword "del":
# del myTuple

#To print the minimum value item in your Tuple...
print(min(myTuple2))
print(max(myTuple2))

#Intro to Dictionaries in Python:
#A dictionary is a collection method which has a Key and Value pair.
# There are no duplicate Keys allowed.

#Creating an Empty Dictionary Version 1
dictionary = {}
print(type(dictionary))

#Creating a Dictionary with Items Version 1:
my_dictionary = {"First_Name": "Shaquille", "Last_Name": "Duggan", "age": 28}
print(my_dictionary)

#You DO NOT look up values in dictionary with Integers Indexes UNLESS the integer index IS the key.
#In which case, you must reference that specific Integer (no real sequence)

#Access a Value
print(my_dictionary["First_Name"]) #-> "Shaquille""
print(my_dictionary["Last_Name"]) #-> "Duggan"
print(type(my_dictionary["age"])) #-> 28

#Dictionaries are mutable data types in Python. Part of the Collection Object.
#This means that I can operate CRUD on it.
# Adding an item to the current dictionary.
my_dictionary["Job_Title"] = "Software Engineer"
print(my_dictionary)

my_dictionary["Favorite_Food"] = "Jamaican Food"
print(my_dictionary)

#Getting Rid of Items in your Dictionary is as simple as:
# my_dictionary.clear()
# print(my_dictionary)

#How do I get the keys from a given or already existing Dictionary?
#You use the .key() method on the Dictionary Object in order to get a tuple of your Keys.
#Because Strings and Tuples are immutable, the list of keys will be displayed as a Tuple.
print(my_dictionary.keys())

#How do I get the values from a gvien or already existing Dictionary?
print(my_dictionary.values())
#The .items() method is better for getting BOTH the keys and the value,
#seperated by commas
print(my_dictionary.items())

#This is useful for problems that require you to submit both an original copy of the dictionary,
#and a copy that is modified.
#The .copy() method is what you use to create a copy of your dictionary
new_dictionary = my_dictionary.copy()
print(new_dictionary)

#Getting rid of single items in your dictionary Version 1:
#You use the .pop() method and specify as an arguement the KEY that you would like to get rid of.
#Its corresponding value is automatically deleted as well.
print(my_dictionary)
my_dictionary.pop("Last_Name")
print(my_dictionary)

#Version 2 of deleting a single item from a dictionary
del my_dictionary["age"]
print(my_dictionary)
