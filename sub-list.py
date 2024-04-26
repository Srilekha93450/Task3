def sub_list_with_zero_sum(nums):
    # Create a set to store the prefix sums
    prefix_sums = set()
    
    # Initialize the prefix sum and add it to the set
    prefix_sum = 0
    prefix_sums.add(prefix_sum)
    
    # Iterate through the list to find sublists with zero sum
    for num in nums:
        prefix_sum += num  # Update the prefix sum
        # Check if the current prefix sum is already in the set
        if prefix_sum in prefix_sums:
            return True  # If found, there exists a sublist with zero sum
        prefix_sums.add(prefix_sum)  # Add the current prefix sum to the set
    
    return False  # If no sublist with zero sum is found, return False

# Given list
nums = [4, 2, -3, 1, 6]

# Call the function to check for sublists with zero sum
result = sub_list_with_zero_sum(nums)

# Print the result
if result:
    print("There is a sublist with sum equal to zero.")
else:
    print("There is no sublist with sum equal to zero.")

