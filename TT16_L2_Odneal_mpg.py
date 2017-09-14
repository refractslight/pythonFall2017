# Name: Susie Odneal
# COSC1336, Lab 2, part 1: Compute MPG
#
# Compute the mileage for a car.

print("This program computes gas mileage.")



# Ask for and get the vehicle make and model.
makeAndModel = input('What is the make and model of the car?')

# Ask for and get the amount of miles travelled.
milesTravelled = int(input('How many miles were travelled?'))
# Ask for and get the number of gallons used.
gallonsUsed = int(input('How many gallons of gas were consumed?'))

# Calculate the gas mileage.
mpg = milesTravelled / gallonsUsed
# Output the results.

# Include: vehicle make and model, miles travelled, gallons used, mileage.
print('Make and model: ', makeAndModel)
print('Miles Travelled: ', milesTravelled)
print('Gallons Used: ', gallonsUsed)
print('Miles per Gallon: ', mpg)
print("Thank you. Be safe.")

# Paste your output below:
## This program computes gas mileage.
## What is the make and model of the car?Toyota Yaris
## How many miles were travelled?10
## How many gallons of gas were consumed?3
## Make and model:  Toyota Yaris
## Miles Travelled:  10
## Gallons Used:  3
## Miles per Gallon:  3.3333333333333335
## Thank you. Be safe.
