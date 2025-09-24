size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Initialize column counter
    col = 0
    
    # Use while loop for columns
    while col < size:
        print("*", end="")
        col += 1
    
    # Move to the next line after completing a row
    print()
    
    # Increment row counter
    row += 1