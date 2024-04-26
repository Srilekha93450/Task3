def find_duplicates(list1, list2, list3):
    # Initialize an empty set to store duplicates
    duplicates = set()
    
    # Iterate through the elements of the first list
    for item in list1:
        # Check if the item is present in both the second and third lists
        if item in list2 and item in list3:
            # If present in all three lists, add it to the set of duplicates
            duplicates.add(item)
    
    return duplicates

# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]

# Call the function to find duplicates
duplicate_items = find_duplicates(list1, list2, list3)

# Print the duplicates
if duplicate_items:
    print("Duplicates:", duplicate_items)
else:
    print("No duplicates found.")
