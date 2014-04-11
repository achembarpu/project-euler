# Checks


import math

from src.custom import params


def is_prime(number):
    """
    Checks if number is prime
    """
    if number == 2:
        return True
    for x in xrange(2, int(math.sqrt(number)+1), 2):
        if number % x == 0:
            return False
    return True


def is_palindrome(thing):
    """
    Checks if the number/string is a palindrome
    """
    if str(thing) == str(thing)[::-1]:
        return True
    else:
        return False


def is_int(number):
    """
    Checks if the float number is essentially an integer
    """
    epsilon = float(number) - int(number)
    if epsilon <= params.float_int_delta:
        return True
    else:
        return False












