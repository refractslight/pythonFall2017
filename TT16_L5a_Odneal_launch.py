# Name: Susie Odneal
# COSC1336, Lab 5a, part 1: Rewrite launch sequence software with functions
#
# Launch a rocket into space.
#
# This program mostly works. It executes the steps required to launch a
# rocket into space. You will improve the program. The output will be
# almost the same, but the launch sequence should not begin until the user
# presses Enter.
#
# BIG PROBLEM!!! It is written without any functions. It has lots and lots
# of redundant code. Identify common blocks of redundant code. Gather the
# redundant code into functions. Eliminate all unneeded extra code.
# Call your functions from main().

# Arrange your program so all output starts in main and ends in main().
# See program 3-3 on page 93, 94 to see an example of how your program
# should be organized.

def welcome():
    print("This program launches a rocket.")
    print("start launch sequence")

def main() :
    welcome()
    input("Press enter to begin the launch sequence...")
    # locate your function calls here in main.
    print('Fill booster fuel tank 1.')
    fuelTanks()
    print('Fill booster fuel tank 2.')
    fuelTanks()
    print('Fill booster fuel tank 3.')
    fuelTanks()
    print('Start engine 1.')
    engineStart()
    print('Start engine 2.')
    engineStart()
    end()

def fuelTanks():
    print("  open valve")
    print("  pre-freeze tank")
    print("  attach filler hose")
    print("  pressurize fuel supply")
    print("  fill tank")
    print("  secure and seal shutoff valve")

def engineStart():
    print("  ignition sequence start")
    print("  start ignition spark generator")
    print("  open fuel valve")
    print("  verify ignition temperature")
    print("  stop ignition spark generator")
    print("  engine 1 is started")

def end():
    print("3, 2, 1, 0, BLASTOFF!!!")
    print("Thank you. Keep looking up!")



main()

# Paste your output below:
# This program launches a rocket.
# start launch sequence
# Press enter to begin the launch sequence...
# Fill booster fuel tank 1.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Fill booster fuel tank 2.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Fill booster fuel tank 3.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Start engine 1.
#   ignition sequence start
#   start ignition spark generator
#   open fuel valve
#   verify ignition temperature
#   stop ignition spark generator
#   engine 1 is started
# Start engine 2.
#   ignition sequence start
#   start ignition spark generator
#   open fuel valve
#   verify ignition temperature
#   stop ignition spark generator
#   engine 1 is started
# 3, 2, 1, 0, BLASTOFF!!!
# Thank you. Keep looking up!