'''This is a beginner level interview problem, which requires some strong fundamentals.'''

# Print out the values 1-100, with the following exceptions:
# If the number is divisible by 3, instead of printing the number, print "fizz".
# If the number is divisible by 5, instead of printing the number, print "buzz".
# If the number is divisible by 3 and 5, print "FizzBuzz".

def fizzbuzz(num = 101):
    ''' # Print out the values 'fizz', 'buzz', or 'FizzBuzz' '''
    if isinstance(num,int):
        for i in range(1, num):
            if(i % 3 == 0 and i % 5 == 0):
                print("FizzBuzz")
            elif i % 3 == 0:
                print("fizz")
            elif i % 5 == 0:
                print("buzz")
            else:
                print(i)

fizzbuzz()
