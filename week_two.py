# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("After appending elements:", my_list)

# Insert value at the second position
my_list.insert(1, 15)

print("After inserting 15 at the second position:", my_list)

# Extend the list with another list
my_list.extend([50, 60, 70])

print("After extending the list:", my_list)

# Remove the last element from the list
my_list.pop()

print("After removing the last element:", my_list)

# Sort the list in ascending order
my_list.sort()

print("After sorting the list:", my_list)

# Find and print the index of the value 30
index = my_list.index(30)

print("Index of the value 30:", index)


