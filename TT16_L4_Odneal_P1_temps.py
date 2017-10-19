#Name: Susie Odneal
# COSC1336, Lab 4

def start():
    print('Hello!\n')
    print('I will help you compute weather statistics for the Austin, Tx area.\n')
    print('Please begin entering temperatures. Press \'q\' to quit.')
    getTemps()

def getTemps():
    total = 0
    sum = 0.0
    response = input("Temperature:")
    if response == 'Q' or response == 'q':
        stats()
    else:
        temp = float(response)
    while temp == int or float:
        total += 1
        sum += temp


def stats():
    print("Number of temperatures entered:", total, "\n")
    print("Highest Temperature:", highestTemp, "\n")
    print("Lowest Temperature:", lowestTemp, "\n")
    print("Average Temperature:", avgTemp, "\n")
    print("Number of Freezing Temperatures", coldTemp, "\n")

start()