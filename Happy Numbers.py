# Function to check if a number is a Happy Number
def is_happy(num):
    # Set to store visited numbers to detect cycles
    visited = set()
    # Iterate until either the number becomes 1 (a happy number) or enters a cycle
    while num != 1 and num not in visited:
        visited.add(num)  # Add the number to the visited set
        num = sum(int(digit)**2 for digit in str(num))  # Calculate the sum of squares of digits
    return num == 1  # Return True if the number is 1 (happy), False otherwise

# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize a variable to count happy numbers
happy_count = 0

# Iterate through each number in the list
for num in numbers:
    # Check if the number is happy
    if is_happy(num):
        # If happy, increment the count
        happy_count += 1

# Print the count of happy numbers
print("Count of Happy Numbers:", happy_count)
