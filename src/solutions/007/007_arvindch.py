#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src.custom import misc


def main():

    giv_n = 10001
    req_num = 0
    
    req_num = misc.nth_prime(giv_n)

    return req_num


if __name__ == '__main__':
    answer = main()
    print answer