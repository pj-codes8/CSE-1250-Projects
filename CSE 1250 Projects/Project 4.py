# Patrick Ordona
# Project 4
# April 2022
# 1250 2:30 PM Lab

# Project 4: State Name and Abbreviation Conversions
# This program asks the user to input the state name or state abbreviation, then output its conversion.

# Program Greeting
print("This program asks the user to input the state name or state abbreviation, then output its conversion.")
print("For users, enter a y or n when prompted.")
print("------------------------------------------------------------------------------------------------------")
print()

# Initial Value:
userInput = "y"

# Loop Process
while userInput == "y":

    # Creating 2 arrays/lists for the state name and abbreviations
    stateNames = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT',
                    'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA',
                    'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN',
                    'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE',
                    'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA',
                    'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS',
                    'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']
        
    stateAbbrev = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL',
                    'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT',
                    'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI',
                    'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    # User Input
    selection = input("Please enter an 'a' for abbreviation or 's' for state name: ")
    selection = selection.lower()
    print()

    # Error Check
    while selection != "a" and selection != "s":
        selection = input("ERROR: Incorrect Input!! Please enter an 'a' or 's' to continue: ")
        selection = selection.lower()
        print()

    # Conditional Check for state names
    if selection == "s":
        searchList = stateAbbrev
        abbreviation = input("Enter the first 2 abbreviation letters of the state: ")
        abbreviation = abbreviation.upper()
        word = abbreviation
        print()

        # While loop to ensure the user types in the correct input of the state name
        while abbreviation not in searchList:
            abbreviation = input("ERROR: Please enter the correct state abbreviation for " + word + ": ")
            abbreviation = abbreviation.upper()
            print()

        # For loop to check the list if the input is found
        for nameIndex in range(len(stateAbbrev)):
            if abbreviation == stateAbbrev[nameIndex]:
                print("The state name for", abbreviation, "is", stateNames[nameIndex].upper())
                print()

    # Conditional Check for state abbreviation
    else:
        searchList = stateNames
        state = input("Enter the name of the state: ")
        state = state.upper()
        word = state
        print()

        # While loop to ensure the user types in the correct input of the state abbreviation
        while state not in searchList:
            state = input("ERROR: Please enter the correct state abbreviation for " + word + ": ")
            state = state.upper()
            print()

        # For loop to check the list if the input is found
        for nameIndex in range(len(stateNames)):
            if state == stateNames[nameIndex]:
                print("The state abbreviation for", state, "is", stateAbbrev[nameIndex].upper())
                print()

    # Input user to run the program again
    userInput = input("Do you want to find another state name or abbreviation again? (y or n): ")
    userInput = userInput.lower()
    print()

    # While loop to ensure the user input types in a "y" or "n"
    while userInput != "y" and userInput != "n":
        userInput = input("ERROR: Incorrect Input!! Please type y or n to continue: ")
        userInput = userInput.lower()
        print()

# Outside of the loop
print("The program has been executed. Have a good day.")
