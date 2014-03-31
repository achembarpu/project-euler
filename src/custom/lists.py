# Lists


from src.custom import gens, params
import itertools


def primes_list(limit=params.prime_lim):
    """
    Returns a list of prime numbers
    """
    primes = list(itertools.takewhile(lambda p: p < limit, gens.primes_gen()))
    return primes