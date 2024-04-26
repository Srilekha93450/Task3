def find_minimum_sorted(nums):
    # Check if the list is empty
    if not nums:
        return None  # Return None if the list is empty
    
    # Return the first element of the list, which is the minimum in a sorted list
    return nums[0]

# Sample sorted list
sorted_list = [1, 2, 3, 4, 5, 6, 7]

# Call the function to find the minimum element
minimum_element = find_minimum_sorted(sorted_list)

# Print the minimum element
if minimum_element is not None:
    print("Minimum element in the sorted list:", minimum_element)
else:
    print("The list is empty.")
