"""
Full Name: Mukesh Ghimire
Class-Section: IS 250-01 Application development program
Assignment Title:Files and Exception Project
Submission Date:11/15/2025
Write your pseudocode here.
 1. Start the program.
 2. Create the calculate_average function.
 3. Ask the user to enter numbers separated by spaces.
 4. Split the input into a list of values.
 5. Convert each value to a number.
 6. Add all the numbers to get a total.
 7. Count how many numbers were entered.
 8. Divide the total by the count to get the average.
 9. Print the average.
 10. End the program.
"""


# Your Python code begins below this line.
# Every line you write must have a comment directly above it.

# Define the calculate_average function
def calculate_average():
    # Ask the user for input
    user_input = input("Enter numbers separated by spaces: ")

    # Split the input into a list
    values = user_input.split()

    # Convert all values to floats
    numbers = [float(x) for x in values]

    # Add the numbers
    total = sum(numbers)

    # Count the numbers
    count = len(numbers)

    # Calculate the average
    average = total / count

    # Print the result
    print("The average is:", average)


# Call the function
calculate_average()


  
