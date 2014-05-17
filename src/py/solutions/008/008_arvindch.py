#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


import data
from src.py.custom import misc


def main():

    giv_str = data.in_str
    giv_num = [int(c) for c in giv_str]
    giv_len = 5
    inf_lim = len(giv_num) - giv_len
    req_prod = 0

    for i in xrange(inf_lim):
        simul_digs = giv_num[i:(i + giv_len)]
        simul_prod = misc.list_product(simul_digs)
        if simul_prod > req_prod:
            req_prod = simul_prod

    return req_prod


if __name__ == '__main__':
    answer = main()
    print answer
