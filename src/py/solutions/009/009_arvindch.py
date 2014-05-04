#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


import math

from src.py.custom import checks, misc


def main():
    
    def pythagorean_triplet_gen(start, end):
        """
        Generates Pythagorean Triplets
        """
        try:
            for a in xrange(start, end):
                for b in xrange(a, end):
                    c = math.sqrt(a ** 2 + b ** 2)
                    if checks.is_int(c):
                        t = [a, b, int(c)]
                        yield t
        except IndexError:
            raise StopIteration
    
    
    giv_sum = 1000
    inf_lim = giv_sum / 2
    req_prod = 0
    
    pythagorean_triplets = pythagorean_triplet_gen(2, inf_lim)
    
    for t in pythagorean_triplets:
        if misc.list_sum(t) == giv_sum:
            req_prod = int(misc.list_product(t))
            break
    return req_prod


if __name__ == '__main__':
    answer = main()
    print answer
