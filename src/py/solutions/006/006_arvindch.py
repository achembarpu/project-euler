#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


def main():

    giv_n = 100
    req_diff = 0

    sum_of_squares = (giv_n * (giv_n + 1) * ((2 * giv_n) + 1)) / 6
    square_of_sum = ((giv_n ** 2) * ((giv_n + 1) ** 2)) / 4
    req_diff = square_of_sum - sum_of_squares

    return req_diff


if __name__ == '__main__':
    answer = main()
    print answer
