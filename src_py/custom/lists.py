# Lists


import math

from src_py.custom import params


def primes_list(limit=params.prime_lim):
    """
    Returns a list of prime numbers
    Using a tweaked Sieve of Eratosthenes method
    """
    half = (limit // 2) + 1
    sieve = [False, True] * half  # preset even nums False
    sieve[1], sieve[2] = False, True
    bound = int(math.sqrt(limit)) + 1  # sqrt is loop bound
    for i in xrange(3, bound, 2):
        if sieve[i]:  # check if prime
            for j in xrange(i ** 2, limit, i):
                sieve[j] = False  # set prime's multiples False
    return [i for i in xrange(limit) if sieve[i]]
