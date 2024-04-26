def first_non_repeating(nums):
    # Create a dictionary to store the frequency of each number
    freq = {}
    
    # Iterate through the list to count the frequency of each number
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if freq[num] == 1:
            return num  # Return the first non-repeating element
    
    # If no non-repeating element is found, return None
    return None

# Sample list of integers
nums = [1, 2, 3, 2, 4, 1, 5, 3, 6]

# Call the function to find the first non-repeating element
result = first_non_repeating(nums)

# Print the result
if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found.")

