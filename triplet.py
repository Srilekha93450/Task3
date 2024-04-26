def find_triplet(nums, target):
    # Sort the list to make it easier to find triplets
    nums.sort()
    
    # Iterate through each element in the list
    for i in range(len(nums) - 2):  # We stop at the third-to-last element to avoid index out of range
        # Set left and right pointers
        left = i + 1
        right = len(nums) - 1
        
        # Iterate while left pointer is less than right pointer
        while left < right:
            # Calculate the sum of the triplet
            triplet_sum = nums[i] + nums[left] + nums[right]
            
            # If the sum equals the target, return the triplet
            if triplet_sum == target:
                return [nums[i], nums[left], nums[right]]
            
            # If the sum is less than the target, move the left pointer forward
            elif triplet_sum < target:
                left += 1
            
            # If the sum is greater than the target, move the right pointer backward
            else:
                right -= 1
    
    # If no triplet is found, return an empty list
    return []

# Given list and target value
nums = [10, 20, 30, 9]
target = 59

# Call the function to find the triplet
triplet = find_triplet(nums, target)

# Print the triplet
if triplet:
    print("Triplet with sum equal to", target, ":", triplet)
else:
    print("No triplet found with sum equal to", target)

