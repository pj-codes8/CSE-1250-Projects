# Patrick Ordona
# Project 5 
# April 2022
# 1250 2:30pm Lab

# Project 5: Unit Conversions using functions
# This program uses the same conversions from project 3, but with functions and a different type of error check.

# Creating a program greeting function
def welcome():
    print("Welcome to the Unit Conversion Program")
    print("This program calculates the unit conversions of the following: Ounces, Grams, Inches, Centimeters, Miles, and Kilometers.")
    print("For users, please type 'y' or 'n' when prompted.")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Instructions for Conversion Type:")
    print("'o'= Grams to Ounces")
    print("'g'= Ounces to Grams")
    print("'i' = Centimeters to Inches")
    print("'c' = Inches to Centimeters")
    print("'m' = Kilometers to Miles")
    print("'k' = Miles to Kilometers")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print()

# Creating the function for the conversion input
def conversionInput():
    unit = input("Enter what units do you want to convert into: ")
    unit = unit.lower()
    print()
    
    while unit != "o" and unit != "g" and unit != "i" and unit != "c" and unit != "m" and unit != "k":
        unit = input("ERROR: Incorrect Unit Type!! Please enter an o, g, i, c, m, or k to continue: ")
        unit = unit.lower()
        print()
        
    return unit

# Creating the function for the conversion calculation
def calculation(unit, value):
    if unit == "o":
        convert_calc = value / 28.3495231
        convert_origin = "grams"
        convert_new = "ounces"
            
    elif unit == "g":
        convert_calc = value * 28.3495231
        convert_origin = "ounces"
        convert_new = "grams"

    elif unit == "i":
        convert_calc = value / 2.54
        convert_origin = "centimeters"
        convert_new = "inches"

    elif unit == "c":
        convert_calc = value * 2.54
        convert_origin = "inches"
        convert_new = "centimeters"

    elif unit == "m":
        convert_calc = value / 1.609344
        convert_origin = "kilometers"
        convert_new = "miles"

    else:
        convert_calc = value * 1.609344
        convert_origin = "miles"
        convert_new = "kilometers"

    return convert_calc, convert_origin, convert_new

# Creating the function that outputs the conversion
def printConversion(value, convert_origin, convert_calc, convert_new):
    print(str(value), convert_origin, "is equal to", format(convert_calc, ",.2f"), convert_new + ".")
    print()

# Creating the function that asks the user to repeat the loop
def repeatLoop():
    runProgram = input("Do you want to enter another conversion type? (y or n): ")
    runProgram = runProgram.lower()
    print()
    
    while runProgram != "y" and runProgram != "n":
        runProgram = input("ERROR: Incorrect Input!! Please enter a y or n to continue: ")
        runProgram = runProgram.lower()
        print()

    return runProgram


#------------ MAIN ------------

# Display the welcome function
welcome()

# Initial variable
loopResult = "y"

# Loop Process
while loopResult == "y":

    # Initial variable for value error
    error = True

    # Loop for value error
    while error == True:

        # Using try/except method to error check the numerical value
        try:
            unitValue = float(input("Enter what number or value you would like to enter: "))
            print()
            break

        except:
            print()
            print("VALUE ERROR DETECTED!! Please enter an integer or decimal(float) value to continue.")
            print()

    # Display the conversion input function
    unit = conversionInput()

    # Display the calculation function
    unitConversion, convertFrom, convertTo = calculation(unit, unitValue)

    # Display the print conversion function
    printConversion(unitValue, convertFrom, unitConversion, convertTo)
    
    # Display the repeat loop function
    loopResult = repeatLoop()

# Display outside the loop
print("The program has been executed. Have a good day.")


