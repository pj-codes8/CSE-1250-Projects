# Patrick Ordona
# Project 1
# February 2022
# 1250 2:30pm Lab

# Project 1: Exponent Calculator
# This program allows the user to input the base and its power on any integer value in addition to returning the exponential result

# Program Greeting
print("This program calculates the exponent of the base and its power using integers only")
print("For users, please type y for yes or n for no when prompted.")
print()

# Initial variable for the loop
loopResult = "y"

# Starting the loop process
while loopResult == "y":

    # Get user input
    baseValue = int(input("Please enter a base: "))
    exponentValue = int(input("To what power of " + str(baseValue) + ": "))
    
    # Calculating the exponent value
    exponentResult = baseValue ** exponentValue

    # Display the output
    print()
    print(baseValue, "raised to the power of", exponentValue, "is", format(exponentResult, ",.0f"))
    print()

    # Getting the user prompt inside the loop
    loopResult = input("Would you like to enter another value? (y or n): ")
    print()

# Display the output ouside the loop
print("Bye, have a good day.")

    

