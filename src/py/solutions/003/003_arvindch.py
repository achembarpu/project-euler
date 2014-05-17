#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


import math

from src.py.custom import lists


def main():

    giv_num = 600851475143
    inf_lim = int(math.sqrt(giv_num))
    req_fact = 0

    prime_nums = lists.primes_list(inf_lim)

    for n in prime_nums:
        if giv_num % n == 0:
            req_fact = n

    return req_fact


if __name__ == '__main__':
    answer = main()
    print answer
