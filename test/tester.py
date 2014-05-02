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
global DEVNULL


def get_answer(file_path, file_name):
    
    global lang
    
    if lang == 'py':
        run_cmd = 'python2 %s/%s' % (file_path, file_name)
    elif lang == 'cpp':
        compile_cmd = 'g++ -o %s/ans.out %s/%s' % (file_path, file_path, file_name)
        subprocess.check_output(compile_cmd.split(' '))  # compile .cpp
        run_cmd = '%s/ans.out' % (file_path)
    elif lang == 'java':
        run_cmd = ''
    
    answer = subprocess.check_output(run_cmd.split(' '))
    
    return answer.strip()


def validation():
    
    global problems
    
    def validator(prob_num):
        
        global dirs, user_name
        
        print '%s:' % prob_num,
        
        # setup solution info
        usr_file = '%s_%s.%s' % (prob_num, user_name, lang)
        prob_dir = '%s/%s' % (dirs['solutions'], prob_num)
        usr_file_path = '%s/%s' % (prob_dir, usr_file)
        ans_file_path = '%s/answer.txt' % (prob_dir)        
        
        # validate problem solution
        try:  # handle missing solution
            with open(usr_file_path, 'r'):
                pass
        except IOError:
            print 'Solution file does not exist!\n'
            return
        
        try:  # handle slow solutions
            with tools.Timeout(test_time):
                solution_out = get_answer(prob_dir, usr_file)
        except excepts.TimeoutError:
            print 'Timed out!\n'
            return
        
        try:  # handle invalid output
            float(solution_out)  # all answers are floats
            str(solution_out)  # filter out error msgs
        except (ValueError, TypeError):
            print 'Invalid output!\n'
            return
        
        try:  # handle non-existent answer.txt
            with open(ans_file_path, 'r') as ansf:
                expect_ans = str(ansf.read())
        except IOError:
            print ans_file_path
            print 'Answer file does not exist!\n'
            return
        
        user_ans = str(solution_out)
        
        if user_ans == expect_ans:
            print 'Valid Answer!\n'
            return
        else:
            print 'Invalid Answer!\n'
            return
    
    
    for prob_num in problems:
        validator(prob_num)


def get_timing(file_path, file_name):
    
    def py_timer(py_file):
    
        # import python file as module
        module_name = py_file[0:-3]
        problem_num = module_name[0:3]
        
        solution = importlib.import_module('src_%s.solutions.%s.%s' % (lang, problem_num, module_name))
        
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
    
    def cpp_timer(file_path, file_name):
        
        sol_file_path = '%s/%s' % (file_path, file_name)
        
        with open('temp.cpp', 'w+') as runfile:
            
            with open(sol_file_path, 'r') as solfile:
                lines = solfile.xreadlines()
                line = next(lines)
                
                while 'using' not in line:
                    runfile.write(line)
                    line = next(lines)
                
                with open('cpp-timer-1.txt', 'r') as cpt1:
                    runfile.write(cpt1.read())
                
                while line != '{\n':
                    line = next(lines)
                line = next(lines)
                
                while 'cout' not in line:
                    runfile.write(line.strip())
                    line = next(lines)
            
            runfile.write('\n')
            with open('cpp-timer-2.txt', 'r') as cpt2:
                runfile.write(cpt2.read())
        
        compile_cmd = 'g++ -o temp.out temp.cpp'
        subprocess.check_output(compile_cmd.split(' '))
        run_cmd = './temp.out'
        exec_time = subprocess.check_output(run_cmd.split(' '))
            
        return exec_time
    
    def java_timer():
        pass
    
    
    if lang == 'py':
        timing_info = py_timer(file_name)
    elif lang == 'cpp':
        timing_info = cpp_timer(file_path, file_name)
    elif lang == 'java':
        timing_info = ''
    
    return timing_info.strip()


def timing():
    
    global user_name, problems, dirs, test_runs
    
    # traverse problems
    for prob_num in problems:  # level 1 - problems
        print '\n%s:\n' % prob_num
        
        # setup dirs
        prob_dir = dirs['solutions'] + '/' + prob_num
        timings_file_path = prob_dir + '/timings.txt'
        
        run_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime())
        
        # open timings.txt to store exec_times
        with open(timings_file_path, 'w+') as timef:
            testing_info = '%s @ %s\n\n' % (user_name, run_time)
            timef.write(testing_info)
            
            for sol_file in os.listdir(prob_dir):  # level 2 - solutions
                # get file extension
                file_ext = sol_file.split('.')[1]
                # ignore non-solutions
                if file_ext == lang and prob_num in sol_file:
                    try:  # handle slow solutions
                        with tools.Timeout(test_time):
                            timing_info = get_timing(prob_dir, sol_file)
                    except excepts.TimeoutError:
                        timing_info = 'Timed out!'
                    exec_info = '%s - %s\n' % (user_name, timing_info)
                    print exec_info[0:-len('\n')]
                    timef.write(exec_info)


def run_test():
    
    global user_name, lang, test_type
    
    print '@%s in %s:\n' % (user_name, lang)
    
    print 'Starting Test...\n'
    
    print '%s started!\n' % test_type['name']
    
    test_type['function']()
    
    print '\n%s complete!\n' % test_type['name']


def setup_test():
    
    def setup_dirs():
        
        global dirs, lang
        
        # setup working dirs
        dirs = {}
        dirs['test'] = os.getcwd()
        dirs['project'] = dirs['test'][0:-len('/test')]
    
    def set_lang():
        
        global dirs, lang
        
        # obtain coding language
        lang_file_path = dirs['test'] + '/lang.txt'
        
        # read from info file - lang.txt
        try:
            with open(lang_file_path, 'r') as langf:
                lang = str(langf.read())
        # or, get and save preferred language for future use
        except IOError:
            print 'Choose programming language: [py, cpp, java]'
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
            print 'Enter User Name:'
            user_name = raw_input('>')
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
        
        global dirs, problems
        
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


def setup_env():
    
    global DEVNULL, dirs
    
    # set null output pipe
    DEVNULL = open(os.devnull, 'w')
    # set PYTHONPATH
    sys.path.append(dirs['project'])


def main():
    
    print 'Test started!\n'
    
    setup_test()
    setup_env()
    run_test()
    
    print 'Test complete!'


if __name__ == '__main__':
    main()
