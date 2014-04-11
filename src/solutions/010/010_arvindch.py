#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src.custom import lists


def main():
    
    giv_lim = 2000000
    req_sum = 0
    
    for prime_num in lists.primes_list(giv_lim):
        req_sum += prime_num
    
    return req_sum


if __name__ == '__main__':
    answer = main()
    print answer