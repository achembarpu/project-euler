#!/usr/bin/env python2.7

import sys
import importlib
import time


# Tweakable Parameters

test_runs = 10


def main():
    
    args = sys.argv
    py_file = args[1]
    module_name = py_file[:-3]
    problem_num = module_name[:3]
    
    solution = importlib.import_module('src.solutions.%s.%s' % (problem_num, module_name))
    
    overall_time = 0.0
    
    for _ in xrange(test_runs):
        
        start_time = time.clock()
        
        solution.main()
        
        end_time = time.clock()
        
        interval_time = end_time - start_time
        overall_time += interval_time
    
    avg_time = float(overall_time / test_runs)
    run_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime())
    
    exec_info = '%s: %s - %s s' % (run_time, py_file, avg_time)
    
    return exec_info


if __name__ == '__main__':
    info = main()
    print info     