# Name: Susie Odneal
# COSC1336
# Exam 1

campus = 'NRG'

def start():
    print('This program calculates enrollment capacity for Austin Community College campuses. \n')
    print('You can:')
    print('[d]isplay detailed instructions')
    print('[c]alculate maximum capacity')
    print('[q]uit\n')
    choice = input('Make a selection:')
    if choice in 'Dd':
        instructions()
    elif choice in 'Cc':
        begin()
    elif choice in 'Qq':
        bye()


def begin():

    global campus
    campus =input('Please enter an ACC campus abbreviation. Enter Q to quit.')
    while campus not in 'Qq':
        getCampusInfo()

def getCampusInfo():
    buildings = int(input('How many buildings on this campus?'))
    classrooms = int(input('How many classrooms in each building?'))
    seats = int(input('How many seats per classroom?'))

    attendance = seats * classrooms * buildings

    print('ACC\'s', campus, "campus can serve up to ", format(attendance, ','), "students.")
    begin()

def instructions():
    print("Enter the ACC campus; enter number of buildings, classrooms, and average seats per classroom,\n" 
          "and this program will output the total seating capacity for that campus.")
    start()

def bye():
    import sys
    sys.exit('Bye!')

start()

# This program calculates enrollment capacity for Austin Community College campuses.
#
# You can:
# [d]isplay detailed instructions
# [c]alculate maximum capacity
# [q]uit
#
# Make a selection:d
# Enter the ACC campus; enter number of buildings, classrooms, and average seats per classroom,
# and this program will output the total seating capacity for that campus.
# This program calculates enrollment capacity for Austin Community College campuses.
#
# You can:
# [d]isplay detailed instructions
# [c]alculate maximum capacity
# [q]uit
#
# Make a selection:c
# Please enter an ACC campus abbreviation. Enter Q to quit.RRC
# How many buildings on this campus?4
# How many classrooms in each building?14
# How many seats per classroom?24
# ACC's RRC campus can serve up to  1,344 students.
# Please enter an ACC campus abbreviation. Enter Q to quit.CYP
# How many buildings on this campus?5
# How many classrooms in each building?15
# How many seats per classroom?25
# ACC's CYP campus can serve up to  1,875 students.
# Please enter an ACC campus abbreviation. Enter Q to quit.ACC
# How many buildings on this campus?6
# How many classrooms in each building?16
# How many seats per classroom?26
# ACC's ACC campus can serve up to  2,496 students.
# Please enter an ACC campus abbreviation. Enter Q to quit.
