##Name: Susie Odneal
# COSC1336, Lab 3, part 3



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

def decide():
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

decide()

# Example Output:
#
#  Welcome to Rock, Paper Scissors!
#
# Choose [r]ock, [p]aper, or [s]cissors.
#
# Player one, please enter your choice.
# r
# Player two, please enter your choice.
# s
# Rock beats scissors. Player one wins!