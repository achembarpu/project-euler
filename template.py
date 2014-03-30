# A Solution Code Template

# Example Q: Check if 101 is prime

# to use pre-written modular functions
import customs
# import other modules, if necessary
import math

# to time solution code
with customs.Timer():
    
    # declare specific functions
    def is_divisible_by(num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False
    
    # declare given data
    giv_num = 101
    # declare inferred data
    inf_lim = int(math.sqrt(giv_num)) + 1
    # declare required data
    req_state = True
    
    # perform operations
    for i in xrange(2, inf_lim):
        if is_divisible_by(giv_num, i):
            req_state = False
            break
    
    # print final data
    if req_state:
        print 'Is prime'
    else:
        print 'Not prime'

        