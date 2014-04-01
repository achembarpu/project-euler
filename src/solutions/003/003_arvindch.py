__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


from src.custom import lists
import math


def main():
    
    giv_num = 600851475143
    inf_lim = int(math.sqrt(giv_num)) + 1
    req_fact = 0

    for prime_num in lists.primes_list(inf_lim):
        if giv_num % prime_num == 0:
            req_fact = prime_num

    return req_fact


if __name__ == '__main__':
    answer = main()
    print answer
