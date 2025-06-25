# Task 1: Basic Mathematical Operations

# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division with error checking
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Displaying the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")


# Task 2: Personalized Greeting

# Taking user's first name and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenating the first name and last name into a full name
full_name = first_name + " " + last_name

# Printing a personalized greeting message
print(f"Hello, {full_name}! Welcome!")
