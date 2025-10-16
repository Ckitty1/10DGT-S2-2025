'''
Author: Luke Low
Date: 17/10/25
Title: "Do you like coffee?"
Version 2.0
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
'''
keep_going = 1

while keep_going == 1:
    
    # asking user if they like coffee or not and recording in variable "ans"
    like_coffee  = input("Do you like coffee? Yes or no? ")

    # printing responses depending on the answer
    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee =="Y" or like_coffee == "y":
        print("Why would you like coffee, it's unnatural")
        keep_going = 0
    elif like_coffee == "no" or like_coffee == "No" or like_coffee == "N" or like_coffee == "n":
        print("That's good, you're natural")
        keep_going = 0
    else:
        print('You need to answer with either "yes" or "no".')
    
    # creating new line for user interface purposes
    print()
'''

# Version 2.0
# Making the program more pythonic

keep_going = ""

while keep_going == "":

    # making the answer as lowercase
    like_coffee = input("Do you like coffee? \n").lower()

    if like_coffee == "yes" or like_coffee == "y":
        print("Why would you like coffee, it's unnatural")
    
    elif like_coffee == "no" or like_coffee == "n":
        print("That's good, you're natural\n")
        

        like_tea = input("Well, do you like tea then? \n").upper()

        if like_tea == "YES" or like_tea == "Y":
            print("\nGood job, tea is more healthy than coffee")
            keep_going = 0

        elif like_tea == "NO" or like_tea == "N":
            print("\nSo what do you drink??")


            like_water = input("Do you like water?\n").upper()

            if like_water == "YES" or like_water == "Y":
                print("\nEh, I guess water is okay")
                keep_going = 0

            elif like_water == "NO" or like_water == "N":
                print("\nWow, you just don't drink anything")
                keep_going = 0

            else:
                print('You need to answer with either "yes" or "no".')

        else:
            print('You need to answer with either "yes" or "no".')

    else:
        print('You need to answer with either "yes" or "no".')

    keep_going = input("\nPress <ENTER> to keep going/restart, otherwise press any other key to exit.")

    # creating new line for user interface purposes
    print()



