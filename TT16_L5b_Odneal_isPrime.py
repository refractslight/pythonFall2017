#Name: Susie Odneal
# COSC1336, Lab 5b, isPrime

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

# Output:
# 14 is composite.
# 52 is composite.
# 43 is prime.
# 60 is composite.
# 3 is prime.
# 32 is composite.
# 22 is composite.
# 62 is composite.
# 19 is prime.
# 5 is prime.