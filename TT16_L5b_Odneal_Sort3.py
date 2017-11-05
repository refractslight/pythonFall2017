#Name: Susie Odneal
# COSC1336, Lab 5b, Sort3
import random

# Decide whether a is greater than b..
def more_than(a, b):
    if a > b:
        return True
    else:
        return False

# Reassign a and b's values
def swap(a, b):
    return b, a

# Sort variables from lowest to highest.
def sort3(a, b, c):

    if more_than(a, b):
        a, b = swap(a, b)
    if more_than(b, c):
        b, c = swap(b, c)

    if more_than(a, b):
        a, b = swap(a, b)

    print('\t Sort to', a, b, c, '\n')

def main():

    for i in range(0, 10):

        #Generate three random numbers
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        print(i + 1,'.) Random numbers:', a, b, c)
        sort3(a, b, c)
        #print('\t Sort to', a, b, c, '\n')
main()