a = int(input("Please provide a number, as an integer."))
b = int(input("Please provide another number, as an integer."))
c = int(input("Lastly provide a final number, as an integer."))
list = a,b,c

sum = sum(list)
print(f'The sum of the numbers you provided is {sum}.')

print(f'The first number minus the second is {a - b}.')

print(f'The third number multiplied by the first is {c * a}.')

print(f'The sum of all three numbers divided by the third number is {sum / c}.')