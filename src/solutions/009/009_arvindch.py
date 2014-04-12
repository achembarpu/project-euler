#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


import math

from src.custom import checks, misc, excepts


def main():
    
    def pythagorean_triplet_gen(start, end):
        """
        Generates Pythagorean Triplets
        """
        try:
            for a in xrange(start, end):
                for b in xrange(start, end):
                    c = math.sqrt(a ** 2 + b ** 2)
                    if checks.is_int(c):
                        triplet = [a, b, int(c)]
                        yield triplet
        except IndexError:
            raise StopIteration
    
    giv_sum = 1000
    inf_lim = giv_sum / 2
    req_prod = 0

    try:
        for triplet in pythagorean_triplet_gen(2, inf_lim):
            if misc.list_sum(triplet) == giv_sum:
                req_prod = int(misc.list_product(triplet))
                raise excepts.BreakNestedLoop
    except excepts.BreakNestedLoop:
        pass
    finally:
        return req_prod


if __name__ == '__main__':
    answer = main()
    print answer
