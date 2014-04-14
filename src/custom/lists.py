# Lists


from src.custom import params


def primes_list(limit=params.prime_lim):
    """
    Returns a list of prime numbers
    Uses the Sieve of Sundaram method
    """
    numbers = range(3, limit, 2)
    half = int(limit / 2)
    initial = 4

    for step in xrange(3, limit, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = None
        initial += 2 * (step + 1)

        if initial > half:
            return [2] + filter(None, numbers)
