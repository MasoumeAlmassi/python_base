# Set up variables and initialize
total = 0
count = 0


# As the user for a number until -1 is entered
while True:
    number = int(input("Enter a number (if you enter -1 it will stop): "))


    # Check if the input is -1 to break the loop - this means it excludes -1 
    if number == -1:
        break
    

    # Add number input to the total
    total += number
    count += 1


# Check the count is more than zero
if count > 0:
    # Calculate the average
    average = total / count
    print(f"The average of the numbers entered is: {average}")
else:
    # In case there is an error or only zeros are entered
    print("No valid numbers were entered.")
    