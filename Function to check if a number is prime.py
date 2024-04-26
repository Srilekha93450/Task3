# Function to check if a number is prime
def is_prime(n):
    if n <= 1:  # Check if the number is less than or equal to 1
        return False
    if n == 2:  # Check if the number is 2
        return True
    if n % 2 == 0:  # Check if the number is even (excluding 2)
        return False
    i = 3
    while i * i <= n:  # Check divisibility up to the square root of n
        if n % i == 0:  # Check if n is divisible by i
            return False  # If divisible, n is not prime
        i += 2  # Increment i by 2 to check only odd numbers
    return True  # If none of the above conditions met, n is prime

# Given list of numbers
numbers = [110, 501, 22, 37, 100, 999, 87, 351]

# Initialize variables to count prime numbers and store them
prime_count = 0
prime_numbers = []

# Iterate through each number in the list
for num in numbers:
    # Check if the number is prime
    if is_prime(num):
        # If prime, increment the count and add it to the prime_numbers list
        prime_count += 1
        prime_numbers.append(num)

# Print the count of prime numbers and the list of prime numbers
print("Count of Prime Numbers:", prime_count)
print("Prime Numbers:", prime_numbers)
