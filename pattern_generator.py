# -------------------------- Half-Diamond Pattern Generator -----------------------------
"""
This program generates half-diamond patterns as seen below:

*
**
***
****
*****
****
***
**
*

Upon startup, the program generates an example of the above pattern for the user to see.
The program then allows the user to generate as many subsequent patterns as they wish,
and allows the user to choose the size of each pattern they generate.

"""


# Display a welcome message for the user.
print("-"*65)
print("Welcome to the Half-Diamond Pattern Generator!")
print("-"*65)

# Display an explanation of the purpose of the program for the user.
print("The program can generate patterns in the shape of a half-diamond.")
print("An example is seen below:")



""" --------------- Display an example of a pattern for the user. ------------------- """

star = "*"

# Print line for spacing - to improve readability.
print()

# Generate and display a half-diamond pattern using the logic within the for-loop.
for i in range(0,9):
    if i<5:
        print(star*(i+1))
    else:
        print(star*(9-i))

# Print line for spacing - to improve readability.
print()


""" -------------- Allow user to generate another pattern or to exit. --------------- """

# Set done variable to False - this will control user exit.
done = False

# Display a divider for readability.
print("-"*50)

# Ask the user if they wish to continue or to exit.
print("Would you like to create another pattern?")
# Request input of an answer from the user.
user_choice = input("Enter 'yes' or 'no':\t")
# Convert to lowercase before input validation.
user_choice = user_choice.lower()


# Perform input validation using a while-loop.
while (user_choice != "yes"):

    if (user_choice == "no"):
        # Set done to True, to allow exit from the program.
        done = True
        # Break the while-loop and return to the main program.
        break

    # If the user enters anything other than "yes" or "no":
    else:
        # Display an error message for the user.
        print("\n*** Invalid Entry ***\n")
        # Request input of another answer from the user.
        user_choice = input("Please enter 'yes' or 'no':\t")
        # Convert new input to lowercase before input validation.
        user_choice = user_choice.lower()


# The below while-loop will generate patterns as long as the user chooses to continue.
while not done:

    # Request input from the user of the pattern length.
    print("\nHow long would you like the pattern to be?")
    pattern_length = int(input("Please enter an odd number:\t"))

    # Ensure the user chooses an odd number to ensure a pointy half-diamond shaped pattern.
    while ((pattern_length % 2) != 1):
        print("\nThe program needs an odd number to give it a nice pattern!\n")
        pattern_length = int(input("Please enter an odd number:\t"))

    # Display a divider for readability.
    print("-"*50)
    print()

    # Generate and display a half-diamond pattern using the length chosen by the user.
    for i in range(0,pattern_length):
        if i<(pattern_length/2):
            print(star*(i+1))
        else:
            print(star*(pattern_length-i))

    # Display a divider for readability.
    print()
    print("-"*50)

    # Ask the user if they wish to generate another pattern or to exit the program.
    print("Would you like to create another pattern?")
    # Request input of an answer from the user.
    user_choice = input("Enter 'yes' or 'no':\t")
    # Convert to lowercase prior to input validation.
    user_choice = user_choice.lower()

    # Perform input validation using a while-loop.
    while (user_choice != "yes"):

        if (user_choice == "no"):
            # Set done to True.
            done = True
            # Break the while-loop to proceed to exit from the main program.
            break

        # If the user enters anything other than "yes" or "no":
        else:
            # Display an error message for the user.
            print("\n*** Invalid Entry ***\n")
            # Request input of another answer from the user.
            user_choice = input("Please enter 'yes' or 'no':\t")
            # Convert to lowercase prior to input validation.
            user_choice = user_choice.lower()


# Display an exit message for the user.
print("-"*50)
print("\nYou have chosen to exit the program. Goodbye.\n")
