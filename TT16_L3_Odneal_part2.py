#Name: Susie Odneal
# COSC1336, Lab 3, part 2

import time
import sys
import random


def start():
    print("|---------- WELCOME TO HAXX0R-TR0N 2k ----------|\n")
    print("What do you want to hack?\n")
    hack = input("Statue of [L]iberty or [S]atellite\n")

    if hack in 'Ll':
        liberty()
    if hack in 'Ss':
        satellite()
    else:
        print('Invalid Entry. Try again.')
        start()

def progress():
    toolbar_width = 40

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(random.uniform(.01,.25))  # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("\n")

    #for i in range(1, 100 + 1):
     #   print(i, '%')
     #   time.sleep(.25)
def liberty():
    print("INFlILTRATING MAINFRAME\n")
    progress()
    end()


def satellite():
    print("INFILTRATING NASA")
    progress()
    print("done")
    time.sleep(1)
    print("Do you want to broadcast a message?\n")
    broadcast = input("[Y]es or [N]o")
    if broadcast in "Yy":
        message()
    if broadcast in "Nn":
        end()
    else:
        print("Invalid entry. Try again.")
        satellite()

def message():
    message = input("Enter broadcast message:")
    progress()
    time.sleep(.2)
    print("Satellite is now broadcasting\"", message,"\"across space.\n")
    end()

def end():
    print("Hacking complete.\n")
    print("Hack again?")
    restart = input("[Y]es or [N]o\n")
    if restart in "Yy":
        start()
    if restart in "Nn":
        import sys
        sys.exit("TERMINATING")

start()

# Output Example
# |---------- WELCOME TO HAXX0R-TR0N 2k ----------|
#
# What do you want to hack?
#
# Statue of [L]iberty or [S]atellite
# S
# INFILTRATING NASA
# [                                        ]
# ----------------------------------------
# done
# Do you want to broadcast a message?
#
# [Y]es or [N]oY
# Enter broadcast message:Hello
# [                                        ]
# ----------------------------------------
# Satellite is now broadcasting" Hello "across space.
#
# Hacking complete.
#
# Hack again?
# [Y]es or [N]o
# Y
# |---------- WELCOME TO HAXX0R-TR0N 2k ----------|
#
# What do you want to hack?
#
# Statue of [L]iberty or [S]atellite
# L
# INFlILTRATING MAINFRAME
#
# [                                        ]
# ----------------------------------------
# Hacking complete.
#
# Hack again?
# [Y]es or [N]o
# N
# TERMINATING