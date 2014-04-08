#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src.custom import gens


def main():
    
    giv_lim = 4000000
    req_sum = 0
    
    for fib_num in gens.fibonacci_gen():
        if fib_num > giv_lim:
            break
        if fib_num % 2 == 0:
            req_sum += fib_num
    
    return req_sum


if __name__ == '__main__':
    answer = main()
    print answer