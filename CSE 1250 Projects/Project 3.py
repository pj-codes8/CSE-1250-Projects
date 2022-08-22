# Patrick Ordona
# Project 3
# March 2022
# 1250 2:30pm Lab

# Project 3: Unit Conversions
# This program is to convert units of the following: Ounces, Grams, Inches, Centimeters, Miles, and Kilometers.

# Program Greeting
print("This program calculates the unit conversions of the following: Ounces, Grams, Inches, Centimeters, Miles, and Kilometers.")
print()
print("For users, please enter o for ounces, g for grams, i for inches, c for centimeters, m for miles, or k for kilometers.")
print()
print("In addition, please enter y or n in the program when prompted")
print()

# Initial Variable
loopResult = "y"

# Loop Process
while loopResult == "y":

    # Getting the user input
    unitValue = float(input("Enter what number or value you would like to enter: "))
    print()
    unit = input("Enter what units do you want to convert into: ")
    unit = unit.lower()
    print()

    # Loop to error check the conversion input
    while unit != "o" and unit != "g" and unit != "i" and unit != "c" and unit != "m" and unit != "k":
        unit = input("ERROR: Incorrect Unit Type!! Please enter an o, g, i, c, m, or k to continue: ")
        unit = unit.lower()
        print()

    # Conditional Statements 
    if unit == "o":
        unitConversion = (unitValue / 28.3495231)
        convertFrom = "grams"
        convertTo = "ounces"
            
    elif unit == "g":
        unitConversion = (unitValue * 28.3495231)
        convertFrom = "ounces"
        convertTo = "grams"

    elif unit == "i":
        unitConversion = (unitValue / 2.54)
        convertFrom = "centimeters"
        convertTo = "inches"

    elif unit == "c":
        unitConversion = (unitValue * 2.54)
        convertFrom = "inches"
        convertTo = "centimeters"

    elif unit == "m":
        unitConversion = (unitValue / 1.609344)
        convertFrom = "kilometers"
        convertTo = "miles"

    else:
        unitConversion = (unitValue * 1.609344)
        convertFrom = "miles"
        convertTo = "kilometers"
        
    # Calculate the unit conversion
    print(str(unitValue), convertFrom, "is equal to", format(unitConversion, ",.2f"), convertTo + ".")
    print()

    # Prompt the user input within the loop
    loopResult = input("Would you like to enter another value? (y or n): ")
    loopResult = loopResult.lower()
    print()
        
    # Loop for error checking incorrect inputs
    while loopResult != "y" and loopResult != "n":
        loopResult = input("ERROR: Incorrect Input!! Please enter a y or n to continue: ")
        loopResult = loopResult.lower()
        print()

# Output outside the loop
print("The program has ended. Have a good day.")
