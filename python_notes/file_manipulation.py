'''File Manipulation'''

#A file is an object on a computer that stores data,
#Information, settings, and/or commands used with a computer program

#An example of a computer program would be is Python File/Module.

#Some advantages of files:
# 1. Data is stored permanently
# 2. Updating can be made easy
# 3. Data can be shared among various programs that also are file objects
# 4. Huge amounts of data can be stored in a file

#Two types of files:
# 1. Text File
# 2. Binary File

#Text Files store the data in the form of "Strings":

'''
"Ram" -> That is stored as 3 characters
234.98 -> That is stored as 6 characters
'''

#Python can do a lot with files.

# Starting with OPENING one:

#Python has a built in method called "open()"

#Example:

'''
myFile = open(<file_name>, <open_mode>)
'''

'''
#1. What is <open_mode>?
#2. What is <file_name> referring to
#3. Are those two "<file_name> <open_mode>" parameter?
#4. Open is a method?
#5. myFile is the variable storing the newly opened file object?
'''

'''
#1. <open_mode> is referring to a character code that grants different privelages to the file that you are currently creating. The different <open_mode>'s are:
    #1.1: "w" -> To write the data. If the file already exists, the data will be overwritten.
    #1.2: "r" -> To read the data. The file pointer is positioned at the beginning of the file
    #1.3: "a" -> To append data to a file. The file pointer is positioned at end of the file.
    #1.4: "w+" -> To write AND read data to/from a file. If the file already exists, the previous data will be overwritten (or lost...)
    #1.5: "r+" -> To read AND write data from/to a file. If the file already exists, your previous data will not be deleted. The file is placed in the beginning of the file.
    #1.6: "a+" -> To append and to read data from a file. The file pointer will be at the end of the file.
    #1.7: "x" -> To open the file in exclusive creation mode. the file creation will FAIL if the file already exists. Meaning this is simply to create the file.
#2. <file_name> is referring to the name you want your file to have. Similar to when we hit "Command+S". We choose a name and an extension. Except we are not using our Computer's Graphic User Interface or OS (Operating System) to accomplish this. We are using pure python.
#3. <file_name> and <open_mode> are the parameters that you substitute with arguments representing what those paramters are expecting
#4. open() indeed is a method that is used to open a file in Python, and it takes in at least two arguments as referenced above with "<file_name> <open_mode>"
#5. myFile indeed is the variable name, and it is assigned the value of the open method with two parameters of "<file_name> <open_mode>"
'''

myFile = open("old_housing.txt", "x")
myFile2 = open("new_housing.txt", "x")
myFile3 = open("moving.txt", "w")
myFile3.write("Whatchu mean, I am ready to move you know what I am saying? ")
myFile3.write("The previous information gets overwritten")
