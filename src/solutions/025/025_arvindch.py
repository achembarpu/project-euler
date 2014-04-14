#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src.custom import gens


def main():
    
    giv_digits = 1000
    req_index = 0
    
    fibs = gens.fibonacci_gen()
    num = next(fibs)
    
    i = 0
    while True:
        num = next(fibs)
        i += 1
        if len(str(num)) == giv_digits:
            req_index = i
            break
    
    return req_index


if __name__ == '__main__':
    answer = main()
    print answer
