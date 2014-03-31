__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


def main():
    
    req_sum = 0
    
    for x in xrange(1000):
        if x % 3 == 0 or x % 5 == 0:
            req_sum += x
    
    return req_sum


if __name__ == '__main__':
    answer = main()
    print answer