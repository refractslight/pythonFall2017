#Name: Susie Odneal
#COSC1336, Lab 3, Part 5

batteryCharged = True
gotCar = True
drunk = False
gas = 2
distance = 100
mpg = 35
nightTime = False
headlightsOut = False
canDrive = False


def start():
    if gotCar and batteryCharged and not drunk and not nightTime and mpg >=(distance/gas) and not headlightsOut:
        canDrive == True
        print("Drive home.")
    elif canDrive == False:
        print("Don't drive home.")

start()

#Output:
#Don't drive home.