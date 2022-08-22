# Patrick Ordona
# Final Project
# May 2022
# 1250 2:30pm Lab

# Final Project
# This program asks the user to either add, delete, edit, view, or repeat the menu of all the contacts listed.

# Creating a Welcome Function
def welcome():
    print("Welcome to the contact manager program.")
    print("---------------------------------------------------------------------------------")
    print("Please,")
    print("Type 'A' to add contacts.")
    print("Type 'E' to edit contacts.")
    print("Type 'D' to delete contacts.")
    print("Type 'L' to view all the list of contacts.")
    print("Type 'H' to show the option list again.")
    print("Type 'X' to exit the program.")
    print("---------------------------------------------------------------------------------")
    print()
    
# Creating a function for adding contacts
def add_contacts(contacts):
    
    # Add contact's name
    name = input("What name would you like to add: ")
    print()

    # Add contact's phone number
    phone_number = input("What phone number would you like to add: ")
    print()

    # Add contact's email
    email = input("What email would you like to add: ")
    print()

    # Add created list
    contacts.append([name, phone_number, email])

    # Confirm added contact
    print("Contact Added")
    print()

    return contacts

# Creating edit function
def edit_contacts(contacts):

    checkList = []
    
    # User Input
    select_edit = input("Would you like to edit the contact by (N)ame, (P)hone Number, or (E)mail: ")
    select_edit = select_edit.upper()
    print()

    # Error Check if the user does not select "N", "P", or "E"
    while select_edit not in ["N", "P", "E"]:
        select_edit = input("ERROR: Not an option!! Please enter 'n', 'p', or 'e' to continue: ")
        select_edit = select_edit.upper()
        print()

    # Edit by name           
    if select_edit == "N":
        name = input("What name would you like to edit: ")
        print()

        # Searches all of the possible names on the nested list
        for mainIndex in contacts:
            checkList.append(mainIndex[0])

        # Iterate while name is not in the contact list
        while name not in checkList:
            print("Name not found. No action taken.")
            print()
            name = input("Please enter the correct name of the contact to edit: ")
            print()
            
        # Iterate to find the element and edit the new name            
        for mainIndex in contacts:
            if name == mainIndex[0]:
                new_name = input("What is the new name for this contact: ")
                mainIndex[0] = new_name
                print()
                print("Contact has been edited.")
                print()

    # Edit by phone number
    elif select_edit == "P":
        phone_number = input("What phone number would you like to edit: ")
        print()

        # Searches all of the possible phone numbers on the nested list
        for mainIndex in contacts:
            checkList.append(mainIndex[1])

        # Iterate while phone number is not in the contact list    
        while phone_number not in checkList:
            print("Phone number not found. No action taken.")
            print()
            phone_number = input("Please enter the correct phone number of the contact to edit: ")
            print()
            
        # Iterate to find the element and edit the new phoe number
        for mainIndex in contacts:
            if phone_number == mainIndex[1]:
                new_phone_number = input("What is the new phone number for this contact: ")
                mainIndex[1] = new_phone_number
                print()
                print("Contact has been edited.")
                print()
                
    # Edit by email
    else:
        email = input("What email would you like to edit: ")
        print()

        # Searches all of the possible emails on the nested list
        for mainIndex in contacts:
            checkList.append(mainIndex[2])

        # Iterate while email is not in the contact list
        while email not in checkList:
            print("Email not found. No action taken.")
            print()
            email = input("Please enter the correct email of the contact to edit: ")
            print()
            
        # Iterate to find the element and edit the new email           
        for mainIndex in contacts:
            if email == mainIndex[2]:
                new_email = input("What is the new email for this contact: ")
                mainIndex[2] = new_email
                print()
                print("Contact has been edited.")
                print()
                        
    return contacts
        
# Creating a function that deletes a listed contacted
def delete_contacts(contacts):

    checkList = []

    # User Input
    delete_select = input("Would you like to delete the contact by (N)ame, (P)hone Number, or (E)mail: ")
    delete_select = delete_select.upper()
    print()

    # Error Check if the user does not select "N", "P", or "E"
    while delete_select not in ["N", "P", "E"]:
        delete_select = input("ERROR: Not an option!! Please enter 'n', 'p', or 'e' to continue: ")
        delete_select = delete_select.upper()
        print()

    # Delete by name
    if delete_select == "N":
        name = input("What name would you like to remove: ")
        print()

        # Searches all of the possible names on the nested list
        for mainIndex in contacts:
            checkList.append(mainIndex[0])

        # Iterate while name is not in the contact list
        while name not in checkList:
            print("Name not found. No action taken.")
            print()
            name = input("Please enter a valid name: ")
            print()

        # Iterate to find the element and delete the contact   
        for mainIndex in contacts:
            if name == mainIndex[0]:
                del mainIndex[2]
                del mainIndex[1]
                del mainIndex[0]
                contacts = list(filter(None, contacts))
                print("Contact Removed.")
                print()

    # Delete by phone number
    elif delete_select == "P":
        phone_number = input("What phone number would you like to remove: ")
        print()

        # Searches all of the possible phone numbers on the nested list
        for mainIndex in contacts:
            checkList.append(mainIndex[1])

        # Iterate while phone number is not in the contact list
        while phone_number not in checkList:
            print("Phone number not found. No action taken.")
            print()
            phone_number = input("Please enter a valid phone number: ")
            print()

        # Iterate to find the element and delete the contact
        for mainIndex in contacts:
            if phone_number == mainIndex[1]:
                del mainIndex[2]
                del mainIndex[1]
                del mainIndex[0]
                contacts = list(filter(None, contacts))
                print("Contact Removed.")
                print()
                
    # Delete by email
    else:
        email = input("What email would you like to remove: ")
        print()

        # Searches all of the possible emails on the nested list
        for mainIndex in contacts:
            checkList.append(mainIndex[2])

        # Iterate while email is not in the contact list
        while email not in checkList:
            print("Email not found. No action taken.")
            print()
            email = input("Please enter a valid email: ")
            print()
            
        # Iterate to find the element and delete the contact       
        for mainIndex in contacts:
            if email == mainIndex[2]:
                del mainIndex[2]
                del mainIndex[1]
                del mainIndex[0]
                contacts = list(filter(None, contacts))
                print("Contact Removed.")
                print()
                    
    return contacts

# Creating a function that views all of the contacts listed
def view_contacts(contacts):

    contactList.sort()

    # Iterate the entire contact list
    for mainIndex in contacts:

        name = mainIndex[0]
        phone_number = mainIndex[1]
        email = mainIndex[2]

        # Display the contact information
        print("-------------------------")
        print("Name:    " + name)
        print("Phone #: " + phone_number)
        print("Email:   " + email)
        print("-------------------------")
        
                    
# Creating the help function
def help_select(select):
    if select == "H":
        welcome()

# Creating a function that allows a user to exit the program
def exit_program(select):
    if select == "X":
        print("You chose to exit the program.")
        print()
        print("Have a good day.")


# -------- Main Program --------

# Display welcome function
welcome()

contactList = [["Bob Smith", "9098815858", "bs@aol.com"],
               ["Mary Wilson", "995558888", "ms@aol.com"],
               ["Will Martin", "7078996666", "wm@aol.com"]]

# User input
selection = input("What would you like to do: ")
selection = selection.upper()
print()

# Error Check
while selection not in ["A", "D", "L", "E", "H", "X"]:
    selection = input("ERROR: Incorrect Input!! Please type an 'A', 'E', 'D', 'L', 'H', or 'X' to continue: ")
    selection = selection.upper()
    print()

# Loop until user chooses "X" to exit the program      
while selection != "X":

    # Calls add function if user selects "A"
    if selection == "A":
        contactList = add_contacts(contactList)
        
    # Calls delete function if user selects "D"
    elif selection == "D":
        contactList = delete_contacts(contactList)
        
    # Calls show list function if user selects "L"    
    elif selection == "L":
        view_contacts(contactList)
        print()
        
    # Calls edit function if user selects "E"    
    elif selection == "E":
        contactList = edit_contacts(contactList)

    # Calls help function if user selects "H"   
    else:
        help_select(selection)
        
    # Grab user input to repeat the main program
    selection = input("What else would you like to do: ")
    selection = selection.upper()
    print()

    # Error Check
    while selection not in ["A", "D", "L", "E", "H", "X"]:
        selection = input("ERROR: Incorrect Input!! Please type an 'A', 'E', 'D', 'L', 'H', or 'X' to continue: ")
        selection = selection.upper()
        print()
        
# Exiting the main program
exit_program(selection)
