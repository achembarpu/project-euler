# Generators


import itertools


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