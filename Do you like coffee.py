'''
Author: Luke Low
Date: 10/10/25
Title: "Do you like coffee?"
Version 1.1
'''

# Version 1.0
'''
# asking user if they like coffee or not and recording in variable "ans"
like_coffee  = input("Do you like coffee? Yes or no? ")

# printing responses depending on the answer
if like_coffee == "yes" or "Yes" or "Y" or "y":
    print("Why would you like coffee, it's unnatural")
elif like_coffee == "no":
    print("That's good, you're natural")
else:
    print('You need to answer with either "yes" or "no".')
'''

# Version 1.1
# Adding loop to rerun the program

keep_going = 1

while keep_going == 1:
    
    # asking user if they like coffee or not and recording in variable "ans"
    like_coffee  = input("Do you like coffee? Yes or no? ")

    # printing responses depending on the answer
    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee =="Y" or like_coffee == "y":
        print("Why would you like coffee, it's unnatural")
    elif like_coffee == "no" or like_coffee == "No" or like_coffee == "N" or like_coffee == "n":
        print("That's good, you're natural")
    else:
        print('You need to answer with either "yes" or "no".')
    
    # creating new line for user interface purposes
    print()
