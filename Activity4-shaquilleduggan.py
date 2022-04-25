"""Variable Name = Variable Value"""
FNAME = "Shaquille"
LNAME = "Duggan"
FAV_COLOR = "black"
MEAL = "fish"

# fstring
print(f"My name is {FNAME} My last name is {LNAME} My favorite color is {FAV_COLOR} My favorite food is {MEAL}")

#Concatenation
FIRSTNAME = "Shaquille"
LASTNAME= "Duggan"
FAV_COLOR_2 = "green"
MEAL2 = "chocolate"

FULLNAME = FIRSTNAME +" "+ LASTNAME
print(FULLNAME)

# or
FULLNAME = FIRSTNAME + LASTNAME
print(FULLNAME)

# or
FULLNAME = f"{FIRSTNAME} {LASTNAME}"
print(FULLNAME)

# Argument by Position

FAV_COLOR_2 = "green"
LASTNAME= " Duggan"
MEAL2 = "chocolate"
FIRSTNAME ="Shaquille"

SENTENCE = "My first name is {0} and My last name is {1} and My favorite color is {2} and My favorite food is {3}".format(FIRSTNAME, LASTNAME, FAV_COLOR_2, MEAL2)
print(SENTENCE)

#Argument by name

SENTENCE7 = "My first name is {FIRSTNAME} and My last name is {LASTNAME} and My favorite color is {FAV_COLOR_2} and My favorite food is {MEAL2}".format(FIRSTNAME = "shaquille", LASTNAME= "duggan", FAV_COLOR_2 = "green", MEAL2 = "hot chocolate")
print(SENTENCE7)
