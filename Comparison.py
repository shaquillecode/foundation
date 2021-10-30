# Arithmetic Operators
# "+"
# "-"
# "*"
# "/" --> divides number on its left by the number on its right and returns a floating value.
# "//" --> divides number on its left by the number on its right, rounds down answer and returns a whole number.
# "**" --> Exponentiation Operator


#Practice with Comparison operators.

#So far the operators we have covered are:
# ">" -->Greater than
# "<" -->Less than
# ">=" -->Greater than or Equal
# "<=" -->Less than or Equal
# "==" --> Equals (Hard Equality)

#Comparison Operators Result in a Boolean Value

# sample1 = 4 > 9
# sample2 = 2 < 4

# print(sample1)
# print(sample2)

#Practice with Logical Operators
#  Solution = False and False
#               print(Solution)


# Praticing with Control Flow or If Statements:
# Step 1: Write the Keyword "if"
# Step 2: Follow it with Parentheses
# Step 3: Put a colon at the end
if(True):
    print("Hello World")
    print("Elvis")
    print("Shaquille".upper())




# The ELSE block ONLY runs when the IF block doesn't
# The IF block doesn't run
    expression1 = 98 > 2000
    expression2 =  23 > 3
    expression3 = "Elon Musk messed up"

    if(expression1):
        print("Elon Musk messed up")

    else:
        print("Elon musk is the greatest!")

    expression4 = 98 > 2000
    expression5 =  23 > 3
    expression6 = "Elon Musk messed up"
    
    if(expression4):
        print("I'm in the IF Statement W00!")
    elif(expression5):
        print("I'm in the ELIF Statement W00!")
    else:
        print("Boo, I'm in the ElSE statement. This means the other two conditions HAVE to have failed.....:(")
    
    
    # a = 10
    # b = 40

    # if a > b:print("A is Greater yeah")
    # else: print("No dummy B is greater")

    # Now we are working with Nested IF/Else Statements:
    if(False):
        print("Hi")
        if(True):
            print("whats up")
        elif(False):
             print("klk")
        else:
            print("What it do")
    else:
        if(False):
            print("bye")
        elif(True):
            print("peace")
        else:
            print("deuces")


    # Creating websites: IF you sign up, you provide some username and password.
    # What happens in the "back-end" is, your username and password get stored in some database owned by that company you signed up for.
    # When you try to log in After you sign up. The process looks literally like this:
        
    # IF username passed in IS EQUAL TO username in database provided at sign up:
             #Provide them their page.

    #ELSE
       #Prompt them to sign back in.
