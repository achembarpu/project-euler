# Lists


import math

from src.custom import params


def primes_list(limit=params.prime_lim):
    """
    Returns a list of prime numbers
    Using a tweaked Sieve of Eratosthenes method
    """
    half = (limit // 2) + 1
    sieve = [False, True] * half
    sieve[1], sieve[2] = False, True
    bound = int(math.sqrt(limit)) + 1
    for i in xrange(3, bound, 2):
        if sieve[i]:
            for j in xrange(i ** 2, limit, i):
                sieve[j] = False
    return [i for i in xrange(limit) if sieve[i]]
