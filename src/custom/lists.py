# Lists


from src.custom import params


def primes_list(limit=params.prime_lim):
    """
    Returns a list of prime numbers
    Using a tweaked Sieve of Eratosthenes method
    """
    half = limit//2
    sieve = [False, True] * half
    sieve[1], sieve[2] = False, True
    i = 3
    while i < half:
        for j in xrange(i*i, limit, i):
            sieve[j] = False
        i += 1
        try:
            while not sieve[i]:
                i += 1
        except IndexError:
            break
    else:
        return [i for i in xrange(limit) if sieve[i]]
