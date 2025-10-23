'''
Author: Luke Low
Date: 22/10/25
Title: Error checking
Version 11.0

Code tht tests whether a valid inout is given
'''

# Code that tests whether a valid input is given (v1.0)
'''
done = False

while not done:
    num = int(input("Please enter your value: "))
    done = True

print(f"The number that you entered was {num}.")'''

# Code that tests whether a valid input is given (v1.1)
# : use the try and except method to catch errors

'''done = False

while not done:
    
    try: # tries for a valid input
        num = float(input("Please enter your value: "))
        done = True

    except ValueError: # responds to an error
        print("That is not a valid float number. \n")

print(f"The number that you entered was {num}.")'''

# Code that tests whether a valid input is given (v1.2)
# : create a function to call every time I ask the user for a number
# Function = "chunk of code that does something"

'''def test_int():
    done = False

    while not done:
        try:
            num = int(input("Please enter your value: "))
            done = True

        except ValueError:
            print("That is not a valid integer. \n")

    print(f"The number that you entered was {num}.")

# MAIN PROGRAM
test_int()'''

# Code that tests whether a valid input is given (v1.3)
# : using the function parameters to make my code more pythonic.

def test_int(question):
    done = False
    error = "That is not a valid integer."

    while not done:
        try:
            num = int(input(f"{question}\n"))
            done = True

        except ValueError:
            print(error)

    return(num)
    
    

# MAIN PROGRAM
num1 = test_int("Please enter your first number: ")
print(f"Your first number you entered is {num1}.\n")

num2 = test_int("Please enter your second number: ")
print(f"Your second number you entered is {num2}.\n")

sum = num1 + num2
print(f"Your two numbers added is {sum}.\n")