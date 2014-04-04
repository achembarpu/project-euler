__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


def main():
    
    giv_num = 100
    req_diff = 0
    
    sum_of_squares = (giv_num * (giv_num + 1) * ((2 * giv_num) + 1)) / 6
    square_of_sums = ((giv_num**2) * ((giv_num + 1)**2)) / 4
    req_diff = square_of_sums - sum_of_squares

    return req_diff


if __name__ == '__main__':
    answer = main()
    print answer