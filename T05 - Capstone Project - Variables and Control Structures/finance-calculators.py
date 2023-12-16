import math

# ask the user to choose investment or bond
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# we will perform the investment calculation
if choice == "investment":
    amount = float(input("The amount of money that you are depositing. "))
    rate = float(input("Enter the interest rate as a percentage, i.e. 8 is 8%. "))
    years = int(input("Enter the number of the years. "))
    interest_type = input("Enter 'simple' or 'compound' for interest calculation: ").lower()
    
    if interest_type == 'simple':
        interest = amount * (1 + (rate / 100) * years)
    elif interest_type == 'compound':
        interest = amount * math.pow((1 + rate / 100), years)
    else:
        print("Invalid input for interest type. Please enter 'simple' or 'compound'.")
    
    print(f"Total amount after {years} years at {rate}% interest is: {interest:.2f}")


# we will perform the bond calculation
elif choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    months = int(input("Enter the number of months to repay the bond: "))
    
    interest = rate / 12 / 100
    bond_repayment = (interest * present_value) / (1 - math.pow(1 + interest, -months))
    
    print(f"The monthly bond repayment will be: {bond_repayment:.2f}")

# error message if invalid input
else:
    print("Invalid input. Please enter 'investment' or 'bond'. ")

