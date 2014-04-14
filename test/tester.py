#!/usr/bin/env python2.7

import importlib
import os
import sys
import time


# Tweakable Parameters

test_runs = 10


global test_dir, proj_dir, ans_dir, user_name


def tester():
    
    global user_name
    
    print 'Starting Test...'
    
    usr_file_path = test_dir + '/user.txt'
    
    try:
        with open(usr_file_path, 'r') as usrf:
            user_name = str(usrf.read())
    except IOError:
        user_name = raw_input('Enter User Name:')
        with open(usr_file_path, 'w+') as usrf:
            usrf.write(user_name)
    
    print 'Validating for %s' % user_name
    
    prob_num = raw_input('Enter Problem Number:')
    
    if validation(prob_num):
        timing()
        print 'Test Success...'
    else:
        print 'Test Failed...'


def validation(prob_num):
    
    global ans_dir
    
    module_path = 'src.solutions.' + prob_num
    user_file = '%s_%s.py' % (prob_num, user_name)
    ans_dir = proj_dir + '/src/solutions/' + prob_num
    ans_file_path = ans_dir + '/answer.txt'
    
    try:
        user_solution = importlib.import_module('%s.%s' % (module_path, user_file[0:-3]))
    except ImportError:
        print 'Invalid Problem Number!'
        return False
    
    print 'Validating solution...'
    
    user_ans = str(user_solution.main())
    
    try:
        with open(ans_file_path, 'r') as ansf:
            expect_ans = str(ansf.read())
    except IOError:
        print 'Create a valid answer.txt!'
        return False
    
    if user_ans == expect_ans:
        print 'Valid Output!'
        return True
    else:
        print 'Invalid Output!'
        return False


def timing():
    
    timings_file_path = ans_dir + '/timings.txt'
    
    run_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime())
    
    with open(timings_file_path, 'w+') as timef:
        testing_info = '%s @ %s\n' % (user_name, run_time)
        timef.write(testing_info)
    
        for pyfile in os.listdir(ans_dir):
            if pyfile[-3:] == '.py' and pyfile[1] != '_':
                print 'Timing %s...' % pyfile
                timing_info = timer(pyfile)
                timef.write('%s\n' % timing_info)
    
    print 'Finished Timing!'
    
    print 'Solution Times:\n'
    with open(timings_file_path, 'r') as timef:
        times = timef.xreadlines()
        next(times)
        for timing in times:
            print timing


def timer(py_file):
    
    module_name = py_file[0:-3]
    problem_num = module_name[0:3]
    
    solution = importlib.import_module('src.solutions.%s.%s' % (problem_num, module_name))
    
    overall_time = 0.0
    
    run_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime())
    
    for _ in xrange(test_runs):
        
        start_time = time.clock()
        
        solution.main()
        
        end_time = time.clock()
        
        interval_time = end_time - start_time
        overall_time += interval_time
    
    avg_time = float(overall_time / test_runs)
    
    exec_info = '%s: %s - %s s' % (run_time, py_file, avg_time)
    
    return exec_info


def main():
    
    global test_dir, proj_dir
    
    test_dir = os.getcwd()
    proj_dir = test_dir[0:-len('/test')]
    
    sys.path.append(proj_dir)
    
    tester()


if __name__ == '__main__':
    main()
