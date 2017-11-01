# Name: Susie Odneal
# COSC1336, Lab 5a, part 3: Demonstrating local scope

# Create a function called add_one(). The function add_one() is very simple. It has one input, a
# parameter called number. It defines one local variable called modified. It adds one to number and
# stores the result in modified. Then it prints: "in add_one. number=xx, modified=yy"
# Make sure you display the actual value of number and modified, not xx and yy.
# Important: AFTER add_one() prints its message, within add_one, call the function times_ten(),
# passing in the parameter modified. It will look like this: times_ten(modified)

def add_one(number):
    modified = number + 1
    print('in add_one, number=', number, 'modified=', modified)
    times_ten(modified)

# Create another function called times_ten(). Function times_ten() is simple, too. It has one input, a
# parameter called number. It defines one local variable called modified. It multiplies number times 10
# and stores the result in modified. Then it prints: "in times_ten. number=xx, modified=yy"
# Important: AFTER times_ten() prints its message, within times_ten, call the function less_100(),
# passing in the parameter modified. It will look like this: less_100(modified)
def times_ten(number):
    modified = number * 10
    print('In times_ten, number=', number, 'modified=', modified)
    less_100(modified)

# Create a third function called less_100(). Function less_100() is trivial. It has one input, a
# parameter called number. It defines one local variable called modified. It subtracts number minus 100
# and stores the result in modified. Then it prints: "in less_100. number=xx, modified=yy"
# The function less_100() does not call anything.
def less_100(number):
    modified = number - 100
    print('in less_100, number=', number, 'modified=', modified)

    
# Almost done. Now create a function main(). In main(), input a number from the user. Store it in
# variable "number". Then call functions: add_one(number), times_ten(number), less_100(number).
# After calling all 3 functions, at the end of main, print: "in main. number=xx"
# Try running your program on the inputs: 10, 100, 1000.
# Notice how number and modified are changed and restored as they "move" through the program.
def main():
    number = int(input('Enter a number'))
    add_one(number)
    times_ten(number)
    less_100(number)
    print('In main, number=', number)

# Call the main function here.
main()
# Paste the output produced for numbers: 10, 100, 1000 below:

# Enter a number10
# in add_one, number= 10 modified= 11
# In times_ten, number= 11 modified= 110
# in less_100, number= 110 modified= 10
# In times_ten, number= 10 modified= 100
# in less_100, number= 100 modified= 0
# in less_100, number= 10 modified= -90
# In main, number= 10

# Enter a number100
# in add_one, number= 100 modified= 101
# In times_ten, number= 101 modified= 1010
# in less_100, number= 1010 modified= 910
# In times_ten, number= 100 modified= 1000
# in less_100, number= 1000 modified= 900
# in less_100, number= 100 modified= 0
# In main, number= 100

# Enter a number1000
# in add_one, number= 1000 modified= 1001
# In times_ten, number= 1001 modified= 10010
# in less_100, number= 10010 modified= 9910
# In times_ten, number= 1000 modified= 10000
# in less_100, number= 10000 modified= 9900
# in less_100, number= 1000 modified= 900
# In main, number= 1000