#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


def main():
    
    giv_num = 2 ** 1000
    req_sum = 0
    
    for digit in str(giv_num):
        req_sum += int(digit)
    
    return req_sum


if __name__ == '__main__':
    answer = main()
    print answer
