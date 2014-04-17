#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


def main():
    
    def digit_gen():
        """
        Generates digits of the natural numbers sequence
        """
        number = 0
        while True:
            number += 1
            for digit in str(number):
                yield int(digit)
    
    
    giv_last_dig = 10 ** 6
    req_prod = 1
    
    digits = digit_gen()
    decimal_const = [next(digits) for _ in xrange(giv_last_dig)]
    
    i = 1
    while i <= giv_last_dig:
        req_prod *= decimal_const[i - 1]
        i *= 10
    
    return req_prod


if __name__ == '__main__':
    answer = main()
    print answer
