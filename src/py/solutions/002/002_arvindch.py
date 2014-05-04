#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src.py.custom import gens


def main():
    
    giv_lim = 4000000
    req_sum = 0
    
    fib_nums = gens.fibonacci_gen()
    
    for n in fib_nums:
        if n > giv_lim:
            break
        if n % 2 == 0:
            req_sum += n
    
    return req_sum


if __name__ == '__main__':
    answer = main()
    print answer
