#!/usr/bin/env python2.7

import os
import sys
import importlib
import time


# Tweakable Parameters

test_runs = 10

global proj_dir, ans_dir


def tester():
    
    print 'Starting Test...'
    
    user_name = raw_input('Enter User Name:')
    prob_num = raw_input('Enter Problem Number:')
    
    if not validation(user_name, prob_num):
        print 'Test Failed...'
        exit()
    else:
        timing()
    
    print 'Test Success...'


def validation(user_name, prob_num):
    
    global ans_dir
    
    print 'Validating solution...'
    
    module_path = 'src.solutions.%s' % prob_num
    
    ans_dir = proj_dir + '/src/solutions' + '/' + prob_num
    user_file = '%s_%s.py' % (prob_num, user_name)
    ans_file_path = ans_dir + '/' + 'answer.txt'
    
    user_solution = importlib.import_module('%s.%s' % (module_path, user_file[:-3]))
    
    user_ans = str(user_solution.main())
    
    with open(ans_file_path, 'r') as ansf:
        expect_ans = str(ansf.read())
        
        if user_ans == expect_ans:
            print 'Valid Output!'
            return True
        else:
            print 'Invalid Output!'
            return False


def timing():
    
    timings_file_path = ans_dir + '/' + 'timings.txt'
    
    for pyfile in os.listdir(ans_dir):
        file_ext = pyfile[-3:]
        if file_ext == '.py' and pyfile[1] != '_':
            print 'Timing %s' % pyfile
            timing_info = timer(pyfile)
            with open(timings_file_path, 'a') as timef:
                timef.write(timing_info + '\n')
    
    print 'Finished Timing!'
    
    print 'Solution Times:'
    with open(timings_file_path, 'r') as timef:
        for line in timef.xreadlines():
            print line


def timer(py_file):
    
    module_name = py_file[0:-3]
    problem_num = module_name[0:3]
    
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


def main():
    
    global proj_dir
    
    test_dir = os.getcwd()
    proj_dir = test_dir[0:-len('/test')]
    sys.path.append(proj_dir)

    tester()


if __name__ == '__main__':
    main()