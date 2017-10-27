# Name:
# COSC1336, Lab 5a, part 3: Demonstrating local scope

# Create a function called add_one(). The function add_one() is very simple. It has one input, a
# parameter called number. It defines one local variable called modified. It adds one to number and
# stores the result in modified. Then it prints: "in add_one. number=xx, modified=yy"
# Make sure you display the actual value of number and modified, not xx and yy.
# Important: AFTER add_one() prints its message, within add_one, call the function times_ten(),
# passing in the parameter modified. It will look like this: times_ten(modified)

def add_one(number):
    modified += 1
    print('in add_one, number=', number, 'modified=', modified)
    times_ten(modified)

# Create another function called times_ten(). Function times_ten() is simple, too. It has one input, a
# parameter called number. It defines one local variable called modified. It multiplies number times 10
# and stores the result in modified. Then it prints: "in times_ten. number=xx, modified=yy"
# Important: AFTER times_ten() prints its message, within times_ten, call the function less_100(),
# passing in the parameter modified. It will look like this: less_100(modified)


# Create a third function called less_100(). Function less_100() is trivial. It has one input, a
# parameter called number. It defines one local variable called modified. It subtracts number minus 100
# and stores the result in modified. Then it prints: "in less_100. number=xx, modified=yy"
# The function less_100() does not call anything.

    
# Almost done. Now create a function main(). In main(), input a number from the user. Store it in
# variable "number". Then call functions: add_one(number), times_ten(number), less_100(number).
# After calling all 3 functions, at the end of main, print: "in main. number=xx"
# Try running your program on the inputs: 10, 100, 1000.
# Notice how number and modified are changed and restored as they "move" through the program.
 
# Call the main function here.

# Paste the output produced for numbers: 10, 100, 1000 below:

