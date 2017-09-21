#Name: Susie Odneal
# COSC1336, Lab 3, part 1

def start():
    print('Good morning!\n')
    print('You wake up to find yourself in your bed.')
    print('Better check the weather so you can get dressed.')
    bedChoice()


def bedChoice():
    print('You can:\n')
    print('Go to the window: [w]')
    print('Go back to sleep: [s]\n')
    getUp = input('What do you do?')
    if getUp =='w':
        window()
    elif getUp == 's':
        bye()
    else:
        print('Invalid entry. Try again.')
        bedChoice()


def window():
    print('You shuffle over to the window.\n')
    print('There is a thermometer here.')
    windowChoice()


def windowChoice():
    print('You can:\n')
    print('Read the thermometer: [t]')
    print('Go back to sleep: [s]\n')
    read = input('What do you do?')
    if read =='t':
        thermometer()
    elif read == 's':
        bye()
    else:
        print('Invalid entry. Try again.')
        windowChoice()


def thermometer():
    print('You squint at the thermometer?')
    temp = int(input('What does it say? It\'s in Farenheits.'))
    if temp <= 60:
        print('It\'s cold! Better take a jacket.')
        rain()
    elif temp >=200:
        print('Apparently you live in a post-apocalyptic world. That isn\'t snow out there - it\'s fallout!\n')
        print('You take your gas-mask, your RadX and your Pip-boy out from storage.\n')
        dressed()
    else:
        print('We don\'t need a jacket today.')
        dressed()

def rain():
    print('After getting your coat, you look out the window again.')
    print('Is it raining?\n')
    raining = input('[y]es or [n]o')
    if raining in 'Yy':
        print('You get an umbrella from the closet.')
        dressed()
    elif raining in 'Nn':
        print('No need for an umbrella!')
        dressed()
    else:
        print('Invalid input. Try again.')
        rain()

def dressed():
    print('You dress and gather your belongings.')
    print('You go to the door and step outside, ready to face the day!')
    end()

def end():
    restart = input('Restart? [y] [n]')
    if restart == 'y':
        start()
    elif restart == 'n':
        die()
    else:
        print('Invalid entry. Try again.')
        end()

def bye():
    print('You decide today is just not worth it, and go back to sleep. Goodnight!\n')
    restart = input('Restart? [y] [n]')
    if restart == 'y' :
        start()
    elif restart == 'n':
        die()
    else:
        print('Invalid entry. Try again.')
        bye()


def die():
    import sys
    sys.exit()


start()

# Good morning!
#
# You wake up to find yourself in your bed.
# Better check the weather so you can get dressed.
# You can:
#
# Go to the window: [w]
# Go back to sleep: [s]
#
# What do you do? w
# You shuffle over to the window.
#
# There is a thermometer here.
# You can:
#
# Read the thermometer: [t]
# Go back to sleep: [s]
#
# What do you do? t

# You squint at the thermometer?
# What does it say? It's in Farenheits. 13

# It's cold! Better take a jacket.
# After getting your coat, you look out the window again.
# Is it raining?
#
# [y]es or [n]o Y

# You get an umbrella from the closet.
# You dress and gather your belongings.
# You go to the door and step outside, ready to face the day!
# Restart? [y] [n]