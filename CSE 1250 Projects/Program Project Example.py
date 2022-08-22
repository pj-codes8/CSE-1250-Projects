# This program adds two numbers and lets the user run the program multiple times

# Program Greeting
print("This program will let you add two numbers of any type.")
print("Please enter a lower case y or n when prompted.")
print()

# Initial Value for the loop
runAgain = "y"

# Start Loop
while runAgain == "y":

    # Get User Input
    firstNumber = float(input("Please enter the first number: "))
    secondNumber = float(input("Please enter the second number: "))

    # Calculate Answer
    answer = firstNumber + secondNumber

    # Display Answer
    print()
    print("The answer is", answer)
    print()

    # Getting user input inside the loop
    runAgain = input("Would you like to add more numbers? (y or n) ")
    print()


print("Have a nice day.")

