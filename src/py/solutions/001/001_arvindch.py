#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


def main():
    
    giv_lim = 1000
    req_sum = 0
    
    for n in xrange(giv_lim):
        if n % 3 == 0 or n % 5 == 0:
            req_sum += n
    
    return req_sum


if __name__ == '__main__':
    answer = main()
    print answer
