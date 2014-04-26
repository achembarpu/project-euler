#!/usr/bin/env python2.7

import importlib
import os
import subprocess
import sys
import time

from src_py.custom import tools, excepts


# Tweakable Parameters
test_time = 60  # seconds
test_runs = 10  # loops

global lang, dirs, user_name, test_type, problems


def validation():
    
    global problems
    
    for prob_num in problems:
        validator(prob_num)


def validator(prob_num):
    
    global dirs, user_name
    
    print '%s:' % prob_num
    
    # import problem solution as module
    module_path = 'src_py.solutions.' + prob_num
    usr_file = '%s_%s' % (prob_num, user_name)
    prob_dir = dirs['solutions'] + '/' + prob_num
    ans_file_path = prob_dir + '/answer.txt'
    
    
    # validate problem solution
    try:  # handle missing solution
        solution = importlib.import_module('%s.%s' % (module_path, usr_file))
    except ImportError:
        print 'Solution file does not exist!\n'
        return
    
    try:  # handle slow solutions
        with tools.Timeout(test_time):
            solution_out = solution.main()
    except excepts.TimeoutError:
        print 'Timed out!\n'
        return
    
    try:  # handle invalid output
        user_ans = str(solution_out)
    except ValueError:
        print 'Invalid output!\n'
        return
    
    try:  # handle non-existent answer.txt
        with open(ans_file_path, 'r') as ansf:
            expect_ans = str(ansf.read())
    except IOError:
        print 'Answer file does not exist!\n'
        return
    
    if user_ans == expect_ans:
        print 'Valid Answer!\n'
        return
    else:
        print 'Invalid Answer!\n'
        return


def timing():
    
    global problems, dirs, test_runs
    
    # level 1 - problems
    for prob_num in problems:
        print '\n%s:\n' % prob_num
        
        # setup dirs
        prob_dir = dirs['solutions'] + '/' + prob_num
        timings_file_path = prob_dir + '/timings.txt'
        
        run_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime())
        
        # open timings.txt to store exec_times
        with open(timings_file_path, 'w+') as timef:
            testing_info = '%s @ %s\n\n' % (user_name, run_time)
            timef.write(testing_info)
            
            # level 2 - solutions
            for py_file in os.listdir(prob_dir):
                # ignore non-solutions
                if py_file[-3:] == '.py' and py_file[1] != '_':
                    try:  # handle slow solutions
                        with tools.Timeout(test_time):
                            timing_info = timer(py_file)
                    except excepts.TimeoutError:
                        timing_info = 'Timed out!'
                    exec_info = '%s - %s\n' % (py_file[4:-3], timing_info)
                    print exec_info[0:-len('\n')]
                    timef.write(exec_info)


def timer(py_file):
    
    # import python file as module
    module_name = py_file[0:-3]
    problem_num = module_name[0:3]
    
    solution = importlib.import_module('src_py.solutions.%s.%s' % (problem_num, module_name))
    
    # initiate times
    overall_time = 0.0
    
    # time main() for test_runs, to get avg time
    for _ in xrange(test_runs):
        
        start_time = time.clock()
        
        solution.main()
        
        end_time = time.clock()
        
        interval_time = end_time - start_time
        overall_time += interval_time
    
    avg_time = overall_time / test_runs
    
    exec_time = '%s s' % avg_time
    
    return exec_time


def run_test():
    
    global user_name, lang, test_type
    
    print '@%s in %s:\n' % (user_name, lang)
    
    print 'Starting Test...\n'
    
    print '%s started!\n' % test_type['name']
    
    test_type['function']()
    
    print '%s complete!\n' % test_type['name']


def setup_test():
    
    def setup_dirs():
        
        global dirs, lang
        
        # setup working dirs
        dirs = {}
        dirs['test'] = os.getcwd()
        dirs['project'] = dirs['test'][0:-len('/test')]
    
    def set_lang():
        
        global dirs, lang
        
        # obtain username
        lang_file_path = dirs['test'] + '/lang.txt'
        
        # read from info file - lang.txt
        try:
            with open(lang_file_path, 'r') as langf:
                lang = str(langf.read())
        # or, get and save preferred language for future use
        except IOError:
            print 'Choose programming language:'
            print '[py, cpp, java]'
            lang = raw_input('>')
            with open(lang_file_path, 'w+') as langf:
                langf.write(lang)
            print ''
        
        # set matching source directory
        dirs['solutions'] = '%s/src_%s/solutions' % (dirs['project'], lang)
    
    def set_user_name():
        
        global dirs, user_name
        
        # obtain username
        usr_file_path = dirs['test'] + '/user.txt'
        
        # read from info file - user.txt
        try:
            with open(usr_file_path, 'r') as usrf:
                user_name = str(usrf.read())
        # or, get and save username for future use
        except IOError:
            user_name = raw_input('Enter User Name:')
            with open(usr_file_path, 'w+') as usrf:
                usrf.write(user_name)
            print ''
    
    def set_test_type():
        
        global test_type
        
        # obtain testing action
        print 'Actions:'
        print 'v - Validate'
        print 't - Time'
        to_run = raw_input('>')
        print ''
        
        # validate choice and setup params
        if to_run == 'v':
            test_type = {'name': 'Validation', 'function': validation}
        elif to_run == 't':
            test_type = {'name': 'Timing', 'function': timing}
        else:
            print 'Invalid choice!'
            print 'Try again...\n'
            set_test_type()
    
    def set_problems():
        
        global problems
        
        # obtain problems
        print 'Problem Numbers: (NNN or all)'
        probs = raw_input('>')
        print ''
        
        problems = []
        
        if probs == 'all':
            for prob_dir in os.listdir(dirs['solutions']):
                problems.append(prob_dir[0:3])
        else:
            for prob in probs.split(' '):
                problems.append(prob)
        
        # for cleaner testing and easier validation
        problems.sort()
        
        # validate problem numbers
        for prob in reversed(problems):  # strings are at list end
            try:
                int(prob)
                break  # when int found, stop
            except ValueError:
                # remove all invalid input
                problems.remove(prob)
                continue
    
    
    setup_dirs()
    set_lang()
    set_user_name()
    set_test_type()
    set_problems()


def main():
    
    print 'Test started!\n'
    
    setup_test()
    run_test()
    
    print 'Test complete!'


if __name__ == '__main__':
    main()
