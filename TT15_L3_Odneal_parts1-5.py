#Name: Susie Odneal
# COSC1336, Lab 3

def start():
    print("Choose which function to perform:\n")
    print("1) Dress for weather")
    print("2) Flowchart")
    print("3)Rock, paper, scissors")
    print("4) Seasons")
    print("5) Drive car\n")
    choice = input("Enter the number of your choice:")

    if choice == "1":
        weather()
    elif choice == "2":
        flowchart()
    elif choice == "3":
        rps()
    elif choice == "4":
        seasons()
    elif choice =="5":
        driveCar()



def weather():
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

import time
import sys
import random


def flowchart():
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


def liberty():
    print("INFlILTRATING MAINFRAME\n")
    progress()
    hackingEnd()


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
        hackingEnd()
    else:
        print("Invalid entry. Try again.")
        satellite()


def message():
    message = input("Enter broadcast message:")
    progress()
    time.sleep(.2)
    print("Satellite is now broadcasting\"", message,"\"across space.\n")
    end()


def hackingEnd():
    print("Hacking complete.\n")
    print("Hack again?")
    restart = input("[Y]es or [N]o\n")
    if restart in "Yy":
        flowchart()
    if restart in "Nn":
        import sys
        sys.exit("TERMINATING")




def rps():
    print("Welcome to Rock, Paper Scissors!\n")
    print("Choose [r]ock, [p]aper, or [s]cissors.\n")
    playerA = input("Player one, please enter your choice.\n")
    if playerA in "Rr":
        choiceA = "rock"
    if playerA in "Pp":
        choiceA = "paper"
    if playerA in "Ss":
        choiceA = "scissors"
    else:
        choiceA = "rock"

    playerB = input("Player two, please enter your choice.\n")
    if playerB in "Rr":
        choiceB = "rock"
    if playerB in "Pp":
        choiceB = "paper"
    if playerB in "Ss":
        choiceB = "scissors"
    else:
        choiceB = "rock"

    if choiceA == choiceB:
        print('Tie game!')

    elif choiceA == "rock":
        if choiceB == "scissors":
            print("Rock beats scissors. Player one wins!")
        if choiceB == "paper":
            print("Paper beats rock. Player two wins!")

    elif choiceA == "scissors":
        if choiceB == "rock":
            print('Rock beats scissors. Player two wins!')
        if choiceB == "paper":
            print("Scissors beat paper. Player one wins!")

    elif choiceA == "paper":
        if choiceB == "rock":
            print("Paper beats rock. Player one wins!")
        if choiceB == "scissors":
            print("Scissors beat paper. Player two wins!")





def seasons():
        season = input("Enter a number, 1 - 4.")
        if season in "1":
            print("Spring is fresh.")

        elif season in "2":
            print("Summer is hot.")

        elif season in "3":
            print("Autumn is cool.")

        elif season in "4":
            print("Winter is cold.")

        elif season not in "1234":
            print("Invalid entry.")
            bye()

        def bye():
            import sys
            sys.exit("Bye!")



def driveCar():
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
        if gotCar and batteryCharged and not drunk and not nightTime and mpg >= (distance / gas) and not headlightsOut:
            canDrive == True
            print("Drive home.")
        elif canDrive == False:
            print("Don't drive home.")




start()