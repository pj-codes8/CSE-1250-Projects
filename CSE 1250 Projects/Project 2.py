# Patrick Ordona
# Project 2
# March 2022
# 1250 2:30pm Lab

# Project 2: Calculate a person's breathing and heartbeat based on their age.
# This program displays a calculation for someone's breathing and heartbeat in terms of their age.

# Program Greeting
print("This program will calculate a person's breathing and heartbeat in terms of their age.")
print("For users, please enter y or n when prompted")
print()

# Initial Variables
loopResult = "y"

# Loop Process
while loopResult == "y":

    # Variables and User Inputs
    minYear = 525600
    age = float(input("What is your age: "))
    print()

    # Check Conditional Statements
    if age >= 15:
        numBreaths = (minYear * 45) + (minYear * 4 * 25) + (minYear * 10 * 20) + (minYear * (age - 15) * 16)

    elif age >= 5 and age <= 14:
        numBreaths = (minYear * 45) + (minYear * 4 * 25) + (minYear * (age - 5) * 20)
       
    elif age >= 1 and age <= 4:
        numBreaths = (minYear * 45) + (minYear * (age - 1) * 25)
         
    else:
        numBreaths = (minYear * age * 45)

    # Calculate the number of heartbeats
    beats_per_min = 67.5
    numHeartbeats = (minYear * age * beats_per_min)

    # Display Calculated Outputs
    print("You have lived for", format(age, ",.0f"), "year(s) with a total of", format(numBreaths, ",.0f"), "breaths.")
    print()
    print("You have a total of", format(numHeartbeats, ",.0f"), "heartbeats.")
    print()
    
    # User input inside the loop
    loopResult = input("Do you want to enter another age value? (y or n): ")
    loopResult = loopResult.lower()
    print()

    # Nested loop for incorrect input
    while loopResult != "y" and loopResult != "n":
        loopResult = input("Error: Incorrect Input!! Please enter y or n: ")
        loopResult = loopResult.lower()
        print()

# Display output outside the loop
print("Bye, have a good day.")
