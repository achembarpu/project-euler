# A Collection of Custom Functions
# for easy usage in Project Euler problems


# Inbuilt Functions

from time import time
import math
import itertools


# Tweakable Parameters


prime_lim = 10**6
float_int_accuracy = 0.00000000001


# Exceptions


class BreakNestedLoop(Exception):
    """
    Raise in a try-except to easily exit a Nested Loop
    """
    pass


# Checks


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
    if epsilon <= float_int_accuracy:
        return True
    else:
        return False


# Generators


def fibonacci_gen():
    """
    Generates Fibonacci Numbers
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primes_gen():
    """
    Generates Prime Numbers
    Uses a tweaked version of Eratosthenes Sieve method
    """
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p


# Lists


def primes_list(limit=prime_lim):
    """
    Returns a list of prime numbers
    """
    primes = list(itertools.takewhile(lambda p: p < limit, primes_gen()))
    return primes


# Miscellaneous


def nth_prime(n):
    """
    Returns the nth prime number
    """
    primes = primes_list(prime_lim)
    return primes[n-1]


def list_product(a_list):
    """
    Returns the product of the items in the list
    """
    prod = 1
    for num in a_list:
        prod *= num
    return prod


def list_sum(a_list):
    """
    Returns the sum of the items in the list
    """
    sm = 0
    for num in a_list:
        sm += num
    return sm


# Tools


class Timer(object):
    """
    A Timer implementation, to easily time code-snippet execution
    """
    def __init__(self):
        self.start = 0.0
        self.end = 0.0
        self.elapsed = 0.0

    def __enter__(self):
        self.start = time()

    def __exit__(self, type, value, traceback):
        self.end = time()
        self.elapsed = self.end - self.start
        print 'exec time = ', self.elapsed