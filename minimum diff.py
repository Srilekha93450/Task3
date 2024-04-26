def distribute_mangoes(bags, students):
    # Sort the bags in ascending order of mangoes
    bags.sort()
    
    min_diff = float('inf')  # Initialize minimum difference to positive infinity
    
    # Iterate through the bags to find the minimum difference
    for i in range(len(bags) - students + 1):
        diff = bags[i + students - 1] - bags[i]  # Calculate difference between max and min mangoes
        min_diff = min(min_diff, diff)  # Update minimum difference
    
    return min_diff

# Input the number of bags
N = int(input("Enter the number of bags: "))

# Input the number of students
M = int(input("Enter the number of students: "))

# Input the number of mangoes in each bag
bags = []
for i in range(N):
    mangoes = int(input("Enter the number of mangoes in bag {}: ".format(i + 1)))
    bags.append(mangoes)

# Call the function to distribute mangoes and find the minimum difference
min_difference = distribute_mangoes(bags, M)

# Print the minimum difference
print("Minimum difference between bags:", min_difference)

