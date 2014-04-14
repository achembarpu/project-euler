# Miscellaneous


from src.custom import lists


def nth_prime(n):
    """
    Returns the nth prime number
    """
    primes = lists.primes_list()
    return primes[n - 1]


def list_product(ls):
    """
    Returns the product of the items in the list
    """
    prod = 1
    for num in ls:
        prod *= num
    return prod


def list_sum(ls):
    """
    Returns the sum of the items in the list
    """
    sm = 0
    for num in ls:
        sm += num
    return sm
