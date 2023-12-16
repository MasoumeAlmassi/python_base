# Import math Library
import math 

print("We are going to calculate the area of a triangle - with lengths that you will provide.")

a = int(input("Please enter a length for side [a]."))
b = int(input("Please enter a length for side [b]."))
c = int(input("Please enter a length for side [c]."))

s = ((a + b +c) / 2)

area = math.sqrt(s * (s-a) * (s-b) * (s-c))

print(f'The area of this triangle is {area}.')