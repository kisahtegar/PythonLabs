# Updating Items

Lists in Python are mutable, meaning you can modify their elements. If you want to update any item in list, First you'll have to select the item using [index] and then change the value inside that.

```py
my_list = [1, 2, 3, 4, 5]

# Update the item at index 2
my_list[2] = 10

print(my_list) # Output: [1, 2, 10, 4, 5]

# ----------------------------
# Create a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row) # Output: [1, 2, 3], [4, 5, 6], [7, 8, 9]

# Update the element at the second row and third column (index 1, 2)
matrix[1][2] = 10

# Print the updated matrix
print("\nUpdated Matrix:")
for row in matrix:
    print(row) # Output: [1, 2, 3], [4, 5, 10], [7, 8, 9]
```
