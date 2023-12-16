# Let's define how many rows and the start/end points
row_count = 5
start = 1
end = (2 * row_count)

# For each row between start and end, we want the star_count
# to be the same as the row number unless is less than or equal to the row count
# in which case it is the end row minus the row number
# then we print * according to the value of star_coumt
for row_number in range(start, end):
    star_count = row_number if row_number <= row_count else end - row_number
    print("* " * star_count)







