#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from py.custom import lists


def main():
    
    giv_lim = 2000000
    req_sum = 0
    
    prime_nums = lists.primes_list(giv_lim)
    
    for n in prime_nums:
        req_sum += n
    
    return req_sum


if __name__ == '__main__':
    answer = main()
    print answer
