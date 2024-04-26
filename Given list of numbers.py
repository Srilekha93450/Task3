# Given list of numbers
numbers = [110, 501, 22, 37, 100, 999, 87, 351]

# Initialize empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through each number in the list
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # If even, append it to the even_numbers list
        even_numbers.append(num)
    else:
        # If odd, append it to the odd_numbers list
        odd_numbers.append(num)

# Print the lists of even and odd numbers
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
