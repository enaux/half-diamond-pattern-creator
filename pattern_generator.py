
"""
This program generates the following pattern:

*
**
***
****
*****
****
***
**
*

It then allows the user to generate as many patterns as they wish, and to choose the size.

"""

print("-"*65)
print("Welcome to the Half-Diamond Pattern Generator!")
print("-"*65)
print("The program can generate patterns in the shape of a half-diamond.")
print("An example is seen below:")




# Initial pattern is printed for the user.
# Additional print() statements are for spacing.
star = "*"

print()

for i in range(0,9):
    if i<5:
        print(star*(i+1))
    else:
        print(star*(9-i))

print()




# Then allow user to choose to generate another pattern or to exit.
        

done = False

# Ask the user to choose either to continue or to exit.
print("-"*50)
print("Would you like to create another pattern?")
user_choice = input("Enter 'yes' or 'no':\t")
user_choice = user_choice.lower()

# while-loop to check if user entry is valid.
while (user_choice != "yes"):
    if (user_choice == "no"):
        # If user chooses no, 'done' is set to True and the below while-loop is never entered.
        # i.e. no more patterns are created.
        done = True
        break
    else:
        print()
        print("*** Invalid Entry ***")
        print()
        user_choice = input("Please enter 'yes' or 'no':\t")
        user_choice = user_choice.lower()


# while-loop will generate patterns for the user as long as they choose to continue.
while not done:

    # Allow the user to choose the pattern size.
    print()
    print("How long would you like the pattern to be?")
    pattern_length = int(input("Please enter an odd number:\t"))

    # Ensure the user chooses an odd number to ensure a pointy half-diamond shaped pattern.
    while ((pattern_length % 2) != 1):
        print()
        print("The program needs an odd number to give it a nice pattern!")
        print()
        pattern_length = int(input("Please enter an odd number:\t"))

    print("-"*50)
    print()

    # Print pattern according to the length chosen by the user.
    for i in range(0,pattern_length):
        if i<(pattern_length/2):
            print(star*(i+1))
        else:
            print(star*(pattern_length-i))

    # Offer the user another choice, to continue or exit.
    print()
    print("-"*50)
    print("Would you like to create another pattern?")
    user_choice = input("Enter 'yes' or 'no':\t")
    user_choice = user_choice.lower()

    # while-loop to check if user entry is valid.
    while (user_choice != "yes"):
        if (user_choice == "no"):
            # If user chooses no, 'done' is set to True to exit the main loop.
            done = True
            break
        else:
            print()
            print("*** Invalid Entry ***")
            print()
            user_choice = input("Please enter 'yes' or 'no':\t")
            user_choice = user_choice.lower()


# Exit message.
print("-"*50)
print()
print("You have chosen to exit the program. Goodbye.")
print()
