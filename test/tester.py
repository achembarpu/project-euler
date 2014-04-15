#!/usr/bin/env python2.7

import importlib
import os
import sys
import time


# Tweakable Parameters

test_runs = 10


global dirs, user_name, problems, is_test


def tester():
    
    print 'Starting Test...'
    
    setup()
    
    print 'Testing for %s:' % user_name
    
    for num in problems:
        if is_test:
            if validator(num):
                timing(num)
            else:
                print 'Test Failed...'
                return None
        else:
            timing(num)
    else:
        print 'Test Successful...'

def setup():
    
    global dirs, user_name, problems, is_test
    
    usr_file_path = dirs['test'] + '/user.txt'
    
    try:
        with open(usr_file_path, 'r') as usrf:
            user_name = str(usrf.read())
    except IOError:
        user_name = raw_input('Enter User Name:')
        with open(usr_file_path, 'w+') as usrf:
            usrf.write(user_name)
    
    prob_nums = raw_input('Enter Problem Numbers:')
    
    problems = []
    
    if prob_nums == 'all':
        is_test = False
        for prob_dir in os.listdir(dirs['solutions']):
            if prob_dir[1] != '_':
                problems.append(prob_dir[0:3])
    else:
        is_test = True
        for num in prob_nums.split(' '):
            problems.append(num)
    

def validator(prob_num):
    
    module_path = 'src.solutions.' + prob_num
    user_file = '%s_%s.py' % (prob_num, user_name)
    prob_dir =  dirs['solutions'] + '/' + prob_num
    ans_file_path = prob_dir + '/answer.txt'
    
    try:
        user_solution = importlib.import_module('%s.%s' % (module_path, user_file[0:-3]))
    except ImportError:
        print 'Invalid Problem Number!'
        return False
    
    print 'Validating solution for %s...' % prob_num
    
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


def timing(prob_num):
    
    prob_dir =  dirs['solutions'] + '/' + prob_num
    timings_file_path = prob_dir + '/timings.txt'
    
    run_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime())
    
    print 'Timing solutions for %s...' % prob_num
    
    with open(timings_file_path, 'w+') as timef:
        testing_info = '%s @ %s\n' % (user_name, run_time)
        timef.write(testing_info)
    
        for pyfile in os.listdir(prob_dir):
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
    
    avg_time = overall_time / test_runs
    
    exec_info = '%s: %s - %s s' % (run_time, py_file, avg_time)
    
    return exec_info


def main():
    
    global dirs
    
    dirs = {}
    
    dirs['test'] = os.getcwd()
    dirs['project'] = dirs['test'][0:-len('/test')]
    dirs['solutions'] = dirs['project'] + '/src/solutions'
    
    sys.path.append(dirs['project'])
    
    tester()


if __name__ == '__main__':
    main()
