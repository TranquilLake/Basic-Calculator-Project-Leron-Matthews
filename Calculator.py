#Note: This program only does calculation with 2 values!
import os

# Function to clear the screen
def clear_output():
    if os.name == 'nt':
        _ = os.system('cls')  # For Windows, clears output
    else:
        _ = os.system('clear')  # For Linux and Mac, also clears output

# Function for addition
def addition(x, y):
    return x + y

# Function for subtraction
def subtraction(x, y):
    return x - y

# Function for multiplication
def multiplication(x, y):
    return x * y

# Function for division
def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Main calculator program code starts here
exit_calculator = False #Sentinel Variable in place to keep program running
result = None

while not exit_calculator:
    clear_output()  # Clear the screen
    #Option screen for desired action/calculation
    print("Basic Calculator Program:") 
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear Output")
    print("6. Exit")

#Keeps the current result on screen until new user input/clearing screen
    if result is not None:
        print("Result: ", result)

    choice = input("Enter your choice: ")

    if choice == '6':
        print("Exiting the calculator. Thanks for trying it out! :)")
        exit_calculator = True #Sentinel variable in place to quit the calculator program
    elif choice == '5':
        result = None 
        input("Output cleared. Press Enter to continue.") #Clears the output/screen, basically resets program
    else:
        value1 = float(input("Enter first number: "))
        value2 = float(input("Enter second number: "))

        if choice == '1':
            result = addition(value1, value2) #adds the 2 given numbers
        elif choice == '2':
            result = subtraction(value1, value2) #subracts value 2 from value 1
        elif choice == '3':
            result = multiplication(value1, value2) #Multiplies value 1 by value 2
        elif choice == '4':
            result = division(value1, value2) #Divides value 1 by value 2
        else:
            print("Invalid choice. Please try again.") #A message to notify an invalid choice was made
            
#That's it! Hope you liked it :)            