###############
# User inputs times #
###############

swim = int(input("In minutes, what time did you record for the swim? "))
print("Swim time, in minutes: ",swim)

cycle = int(input("In minutes, what time did you record for the cycle? "))
print("Cycle time, in minutes: ",cycle)

run = int(input("In minutes, what time did you record for the run? "))
print("Run time, in minutes: ",run)

#########################
# Calculate total time  and award #
#########################

total_time=swim+cycle+run
print("Total triathlon time, in minutes: ",total_time)

if (total_time < 100):
 print("Provincial Colors")
elif (total_time > 100 and total_time <=105):
 print("Provincial Half Colors")
elif(total_time > 105 and total_time <=110):
 print("Provincial Scroll")
else:
 print("No award")
 
 
