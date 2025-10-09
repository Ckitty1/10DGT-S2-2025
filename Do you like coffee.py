'''
Author: Luke Low
Date: 10/10/25
Title: "Do you like coffee?"
Version 1.0
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