#Name: Susie Odneal
# COSC1336, Lab 4, part 3

import random

def main():
    for i in range(0, 10):
        num = random.randint(1, 100)
        i += 1
        isPrime(num)

def isPrime(num):
    #num = int(input('Enter a positive integer to check and see if it\'s prime. 0 to quit'))
    is_prime = True
    i = 2

    if num == 0:
        bye()

    while i < num:

        if num % i == 0:
            is_prime = False
            break
        else:
            i += 1
    if is_prime:
        print(num, 'is prime.')
    else:
        print(num, 'is composite.')
    return is_prime

def bye():
    print('Goodbye.')


main()