#!/usr/bin/env python2.7

__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


import data


def main():

    giv_mat = data.in_mat
    for i in xrange(20):
        for j in xrange(20):
            giv_mat[i][j] = int(giv_mat[i][j])
    req_prod = 0

    for i in xrange(20):
        for j in xrange(20):
            products = {'horizontal': 0, 'vertical': 0, 'down_diag': 0, 'up_diag': 0}
            # horizontal products
            try:
                products['horizontal'] = giv_mat[i][j] * giv_mat[i][j + 1] * giv_mat[i][j + 2] * giv_mat[i][j + 3]
            except IndexError:
                products['horizontal'] = 0
            # vertical products
            try:
                products['vertical'] = giv_mat[i][j] * giv_mat[i + 1][j] * giv_mat[i + 2][j] * giv_mat[i + 3][j]
            except IndexError:
                products['vertical'] = 0
            # diagonal products
            try:
                products['down_diag'] = giv_mat[i][j] * giv_mat[i + 1][j + 1] * giv_mat[i + 2][j + 2] * giv_mat[i + 3][j + 3]
            except IndexError:
                products['down_diag'] = 0
            try:
                products['up_diag'] = giv_mat[i][j] * giv_mat[i - 1][j + 1] * giv_mat[i - 2][j + 2] * giv_mat[i - 3][j + 3]
            except IndexError:
                products['up_diag'] = 0

            # compare products
            for product in products.values():
                if product > req_prod:
                    req_prod = product

    return req_prod


if __name__ == '__main__':
    answer = main()
    print answer
