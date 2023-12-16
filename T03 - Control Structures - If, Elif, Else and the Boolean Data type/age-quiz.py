'''
I had to reorder the if-elif-else statements in descending order (100 to 13) to make sure logic is correct.
'''

# ask for iput
age = int(input('Please enter your age.'))

# if the user enters a higher number
if  age > 100:
     print ("Sorry, you're dead.")
     
# if the user is 65 or older
elif age >= 65:
    print ("Enjoy your retirement!")

# if the user is 40 or over
elif age >= 40:
     print ("You're over the hill.")

# if the user is 21
elif age == 21:
    print ("Congrats on your 21st!")

# If the user is under 13
elif age < 13:
    print ("You qualify for the kiddie discount.")

else:
    print ("Age is but a number")