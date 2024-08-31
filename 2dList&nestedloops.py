# Define a 2D list (list of lists)
num_grid = [
    [1, 2, 3],  # Row 0: contains 1, 2, 3
    [4, 5, 6],  # Row 1: contains 4, 5, 6
    [7, 8, 9],  # Row 2: contains 7, 8, 9
    [0]         # Row 3: contains a single value 0
]

# Print specific elements in num_grid
print(num_grid[0][0])   # Print value in the zeroth row, zeroth column (value: 1)
print(num_grid[1][0])   # Print value in the first row, zeroth column (value: 4)
print(num_grid[2][2])   # Print value in the second row, second column (value: 9....


print("using nested for loops")
for row in num_grid :
   for col in row:
    print(col)