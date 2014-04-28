#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src_py.custom import gens


def main():
    
    giv_digits = 1000
    req_index = 0
    
    fibs = gens.fibonacci_gen()
    next(fibs)  # skip 0
    
    i = 1
    for n in fibs:
        if len(str(n)) == giv_digits:
            req_index = i
            break
        i += 1
    
    return req_index


if __name__ == '__main__':
    answer = main()
    print answer
