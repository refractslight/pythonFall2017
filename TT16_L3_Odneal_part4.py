#Name: Susie Odneal
#COSC1336, Lab 3, part 4

def start():
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

start()


#Outputs:
#Enter a number, 1 - 4.1
#Spring is fresh.
#
#Enter a number, 1 - 4.2
#Summer is hot.
#
#Enter a number, 1 - 4.3
#Autumn is cool.
#
#Enter a number, 1 - 4.4
#Winter is cold.
#
#Enter a number, 1 - 4.p
#Invalid entry.
#Bye!