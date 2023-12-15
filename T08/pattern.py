pattern.py

# Define the number of rows for the pattern
rows = 9  # Adjust this number to change the height of the pattern


# Loop to iterate through each row
for i in range(1, rows + 1):
    if i <= (rows // 2) + 1:

        # For the first half of the pattern
        for j in range(i):
            print('*', end='')
            
    else:
        # For the second half of the pattern
        for j in range(rows - i + 1):
            print('*', end='')

    # Move to the next line after each row is printed, except for the last iteration
    if i != rows:
        print()



