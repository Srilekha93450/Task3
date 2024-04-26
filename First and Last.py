# Function to find the sum of the first and last digit of an integer
def sum_first_last_digit(n):
    # Convert the integer to a string to access individual digits
    num_str = str(n)
    
    # Extract the first and last digits from the string
    first_digit = int(num_str[0])  # Convert the first character to an integer
    last_digit = int(num_str[-1])  # Convert the last character to an integer
    
    # Calculate the sum of the first and last digits
    sum_digits = first_digit + last_digit
    
    # Return the sum
    return sum_digits

# Input an integer from the user
num = int(input("Enter an integer: "))

# Call the function to find the sum of the first and last digit
result = sum_first_last_digit(num)

# Print the result
print("Sum of first and last digit:", result)
